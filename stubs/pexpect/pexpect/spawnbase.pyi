import io
import re
from _typeshed import Incomplete, Self, SupportsWrite
from collections.abc import Awaitable, Callable, Iterable, Iterator
from types import TracebackType
from typing import AnyStr, Generic, TypeVar, overload
from typing_extensions import Literal, TypeAlias

from .exceptions import EOF, TIMEOUT

PY3: bool
text_type: Callable[[Incomplete], Incomplete]

class _NullCoder:
    @staticmethod
    def encode(b: bytes, final: bool = False) -> bytes: ...
    @staticmethod
    def decode(b: bytes, final: bool = False) -> bytes: ...

class _SupportsWriteFlush(SupportsWrite[AnyStr]):
    def flush(self) -> object: ...

_BufferType = TypeVar("_BufferType", io.StringIO, io.BytesIO)

_Pattern: TypeAlias = str | AnyStr | re.Pattern[AnyStr] | type[EOF | TIMEOUT]
_CompiledPattern: TypeAlias = re.Pattern[AnyStr] | type[EOF | TIMEOUT]
_ExactPattern: TypeAlias = str | AnyStr | type[EOF | TIMEOUT]

_Patterns: TypeAlias = Iterable[_Pattern[AnyStr]] | _Pattern[AnyStr] | None
_ExactPatterns: TypeAlias = Iterable[_ExactPattern[AnyStr]] | _ExactPattern[AnyStr]

class SpawnBase(Generic[AnyStr, _BufferType]):
    encoding: str | None
    pid: int | None
    flag_eof: bool
    stdin: Incomplete
    stdout: Incomplete
    stderr: Incomplete
    searcher: Incomplete
    ignorecase: bool
    before: AnyStr
    after: AnyStr
    match: re.Match[AnyStr]
    match_index: int | None
    terminated: bool
    exitstatus: int | None
    signalstatus: int | None
    status: int | None
    child_fd: int
    timeout: float | None
    delimiter: Incomplete
    logfile: _SupportsWriteFlush[AnyStr]
    logfile_read: _SupportsWriteFlush[AnyStr]
    logfile_send: _SupportsWriteFlush[AnyStr]
    maxread: int
    searchwindowsize: int | None
    delaybeforesend: float
    delayafterclose: float
    delayafterterminate: float
    delayafterread: float
    softspace: bool
    name: str
    closed: bool
    codec_errors: str | None
    string_type: type[AnyStr]
    buffer_type: type[_BufferType]
    crlf: AnyStr
    allowed_string_types: tuple[type[bytes | str], ...]
    linesep: AnyStr
    write_to_stdout: Callable[[AnyStr], int]
    async_pw_transport: Incomplete
    @overload
    def __init__(
        self: SpawnBase[bytes, io.BytesIO],
        timeout: float | None = 30,
        maxread: int = 2000,
        searchwindowsize: int | None = None,
        logfile: _SupportsWriteFlush[bytes] | None = None,
        encoding: None = None,
        codec_errors: str = "strict",
    ): ...
    @overload
    def __init__(
        self: SpawnBase[str, io.StringIO],
        timeout: float | None,
        maxread: int,
        searchwindowsize: int | None,
        logfile: _SupportsWriteFlush[str] | None,
        encoding: str,
        codec_errors: str = "strict",
    ): ...
    @overload
    def __init__(
        self: SpawnBase[str, io.StringIO],
        timeout: float | None = 30,
        maxread: int = 2000,
        searchwindowsize: int | None = None,
        logfile: _SupportsWriteFlush[str] | None = None,
        *,
        encoding: str,
        codec_errors: str = "strict",
    ): ...
    buffer: AnyStr
    def read_nonblocking(self, size: int = 1, timeout: float | None = None) -> AnyStr: ...
    def compile_pattern_list(self, patterns: _Patterns[AnyStr]) -> list[_CompiledPattern[AnyStr]]: ...
    @overload
    def expect(
        self,
        pattern: _Patterns[AnyStr],
        timeout: float | None = -1,
        searchwindowsize: int = -1,
        *,
        async_: Literal[False] = False,
    ) -> int: ...
    @overload
    def expect(
        self, pattern: _Patterns[AnyStr], timeout: float | None = -1, searchwindowsize: int = -1, *, async_: Literal[True]
    ) -> Awaitable[int]: ...
    @overload
    def expect_list(
        self,
        pattern_list: Iterable[_CompiledPattern[AnyStr]],
        timeout: float | None = -1,
        searchwindowsize: int = -1,
        *,
        async_: Literal[False] = False,
    ) -> int: ...
    @overload
    def expect_list(
        self,
        pattern_list: Iterable[_CompiledPattern[AnyStr]],
        timeout: float | None = -1,
        searchwindowsize: int = -1,
        *,
        async_: Literal[True],
    ) -> Awaitable[int]: ...
    @overload
    def expect_exact(
        self,
        pattern_list: _ExactPatterns[AnyStr],
        timeout: float | None = -1,
        searchwindowsize: int = -1,
        *,
        async_: Literal[False] = False,
    ) -> int: ...
    @overload
    def expect_exact(
        self,
        pattern_list: _ExactPatterns[AnyStr],
        timeout: float | None = -1,
        searchwindowsize: int = -1,
        *,
        async_: Literal[True],
    ) -> Awaitable[int]: ...
    def expect_loop(self, searcher: Incomplete, timeout: float | None = -1, searchwindowsize: int = -1) -> int: ...
    def read(self, size: int = -1) -> AnyStr: ...
    def readline(self, size: int = -1) -> AnyStr: ...
    def __iter__(self) -> Iterator[AnyStr]: ...
    def readlines(self, sizehint: int = -1) -> list[AnyStr]: ...
    def fileno(self) -> int: ...
    def flush(self) -> None: ...
    def isatty(self) -> bool: ...
    def __enter__(self: Self) -> Self: ...
    def __exit__(self, etype: type[BaseException] | None, evalue: BaseException | None, tb: TracebackType | None) -> None: ...
