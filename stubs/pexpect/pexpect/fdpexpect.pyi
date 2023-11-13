from _typeshed import FileDescriptorLike, Incomplete
from collections.abc import Iterable
from typing import AnyStr, Literal, NoReturn, overload

from .spawnbase import SpawnBase, _SupportsWriteFlush

class fdspawn(SpawnBase[AnyStr]):
    args: None
    command: None
    own_fd: Literal[False]
    use_poll: bool
    @overload
    def __init__(
        self: fdspawn[bytes],
        fd: FileDescriptorLike,
        args: Incomplete | None = None,
        timeout: float | None = 30,
        maxread: int = 2000,
        searchwindowsize: int | None = None,
        logfile: _SupportsWriteFlush[bytes] | None = None,
        encoding: None = None,
        codec_errors: str = "strict",
        use_poll: bool = False,
    ) -> None: ...
    @overload
    def __init__(
        self: fdspawn[str],
        fd: FileDescriptorLike,
        args: Incomplete | None = None,
        timeout: float | None = 30,
        maxread: int = 2000,
        searchwindowsize: int | None = None,
        logfile: _SupportsWriteFlush[str] | None = None,
        *,
        encoding: str,
        codec_errors: str = "strict",
        use_poll: bool = False,
    ) -> None: ...
    @overload
    def __init__(
        self: fdspawn[str],
        fd: FileDescriptorLike,
        args: Incomplete | None,
        timeout: float | None,
        maxread: int,
        searchwindowsize: int | None,
        logfile: _SupportsWriteFlush[str] | None,
        encoding: str,
        codec_errors: str = "strict",
        use_poll: bool = False,
    ) -> None: ...
    def close(self) -> None: ...
    def isalive(self) -> bool: ...
    def terminate(self, force: bool = False) -> NoReturn: ...
    def send(self, s: AnyStr | str) -> int: ...
    def sendline(self, s: AnyStr | str) -> int: ...
    def write(self, s: AnyStr | str) -> None: ...
    def writelines(self, sequence: Iterable[AnyStr | str]) -> None: ...
    def read_nonblocking(self, size: int = 1, timeout: float | None = -1) -> AnyStr: ...
