import io
import sys
from _typeshed import StrOrBytesPath
from collections.abc import Callable, Iterable, Mapping
from typing import AnyStr, overload
from typing_extensions import TypeAlias

from .spawnbase import SpawnBase, _BufferType, _SupportsWriteFlush

# _ENV copied from subprocess.pyi
if sys.platform == "win32":
    _ENV: TypeAlias = Mapping[str, str]
else:
    _ENV: TypeAlias = Mapping[bytes, StrOrBytesPath] | Mapping[str, StrOrBytesPath]

PY3: bool

class spawn(SpawnBase[AnyStr, _BufferType]):
    use_native_pty_fork: bool
    STDIN_FILENO: int
    STDOUT_FILENO: int
    STDERR_FILENO: int
    str_last_chars: int
    env: _ENV
    command: str
    args: list[AnyStr]

    @overload
    def __init__(
        self: spawn[bytes, io.BytesIO],
        command: str,
        args: list[bytes] = [],
        timeout: float | None = 30,
        maxread: int = 2000,
        searchwindowsize: int | None = None,
        logfile: _SupportsWriteFlush[bytes] | None = None,
        cwd: StrOrBytesPath | None = None,
        env: _ENV | None = None,
        ignore_sighup: bool = False,
        echo: bool = True,
        preexec_fn: Callable[[], object] | None = None,
        encoding: None = None,
        codec_errors: str = "strict",
        dimensions: tuple[int, int] | None = None,
        use_poll: bool = False,
    ) -> None: ...
    @overload
    def __init__(
        self: spawn[str, io.StringIO],
        command: str,
        args: list[str] = [],
        timeout: float | None = 30,
        maxread: int = 2000,
        searchwindowsize: int | None = None,
        logfile: _SupportsWriteFlush[str] | None = None,
        cwd: StrOrBytesPath | None = None,
        env: _ENV | None = None,
        ignore_sighup: bool = False,
        echo: bool = True,
        preexec_fn: Callable[[], object] | None = None,
        codec_errors: str = "strict",
        dimensions: tuple[int, int] | None = None,
        use_poll: bool = False,
        *,
        encoding: str,
    ) -> None: ...
    @overload
    def __init__(
        self: spawn[str, io.StringIO],
        command: str,
        args: list[str],
        timeout: float | None,
        maxread: int,
        searchwindowsize: int | None,
        logfile: _SupportsWriteFlush[str] | None,
        cwd: StrOrBytesPath | None,
        env: _ENV | None,
        ignore_sighup: bool,
        echo: bool,
        preexec_fn: Callable[[], object] | None,
        encoding: str,
        codec_errors: str = "strict",
        dimensions: tuple[int, int] | None = None,
        use_poll: bool = False,
    ) -> None: ...
    def close(self, force: bool = True) -> None: ...
    def isatty(self) -> bool: ...
    def waitnoecho(self, timeout: float | None = -1) -> None: ...
    def getecho(self) -> bool: ...
    def setecho(self, state: bool) -> None: ...
    def read_nonblocking(self, size: int = 1, timeout: float | None = -1) -> AnyStr: ...
    def write(self, s: AnyStr | str) -> None: ...
    def writelines(self, sequence: Iterable[AnyStr | str]) -> None: ...
    def send(self, s: AnyStr | str) -> int: ...
    def sendline(self, s: AnyStr | str = "") -> int: ...
    def sendcontrol(self, char: str) -> int: ...
    def sendeof(self) -> None: ...
    def sendintr(self) -> None: ...
    @property
    def flag_eof(self) -> bool: ...
    @flag_eof.setter
    def flag_eof(self, value: bool) -> None: ...
    def eof(self) -> bool: ...
    def terminate(self, force: bool = False) -> bool: ...
    def wait(self) -> int: ...
    def isalive(self) -> bool: ...
    def kill(self, sig: int) -> None: ...
    def getwinsize(self) -> tuple[int, int]: ...
    def setwinsize(self, rows: int, cols: int) -> None: ...
    def interact(
        self,
        escape_character: str = "\x1d",
        input_filter: Callable[[bytes], bytes] | None = None,
        output_filter: Callable[[bytes], bytes] | None = None,
    ) -> None: ...

def spawnu(
    command: str,
    args: list[str] = [],
    timeout: float | None = 30,
    maxread: int = 2000,
    searchwindowsize: int | None = None,
    logfile: _SupportsWriteFlush[str] | None = None,
    cwd: StrOrBytesPath | None = None,
    env: _ENV | None = None,
    ignore_sighup: bool = False,
    echo: bool = True,
    preexec_fn: Callable[[], object] | None = None,
    encoding: str = "utf-8",
    codec_errors: str = "strict",
    dimensions: tuple[int, int] | None = None,
    use_poll: bool = False,
) -> None: ...
