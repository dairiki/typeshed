import io
import subprocess
from _typeshed import StrOrBytesPath
from collections.abc import Callable, Iterable
from typing import AnyStr, overload

from .spawnbase import SpawnBase, _BufferType, _SupportsWriteFlush

class PopenSpawn(SpawnBase[AnyStr, _BufferType]):
    proc: subprocess.Popen
    pid: int | None
    terminated: bool
    exitstatus: int | None
    signalstatus: int | None

    @overload
    def __init__(
        self: PopenSpawn[bytes, io.BytesIO],
        cmd: subprocess._CMD,
        timeout: float | None = 30,
        maxread: int = 2000,
        searchwindowsize: int | None = None,
        logfile: _SupportsWriteFlush[bytes] | None = None,
        cwd: StrOrBytesPath | None = None,
        env: subprocess._ENV | None = None,
        encoding: None = None,
        codec_errors: str = "strict",
        preexec_fn: Callable[[], object] | None = None,
    ) -> None: ...
    @overload
    def __init__(
        self: PopenSpawn[str, io.StringIO],
        cmd: subprocess._CMD,
        timeout: float | None,
        maxread: int,
        searchwindowsize: int | None,
        logfile: _SupportsWriteFlush[str] | None,
        cwd: StrOrBytesPath | None,
        env: subprocess._ENV | None,
        encoding: str,
        codec_errors: str = "strict",
        preexec_fn: Callable[[], object] | None = None,
    ) -> None: ...
    @overload
    def __init__(
        self: PopenSpawn[str, io.StringIO],
        cmd: subprocess._CMD,
        timeout: float | None = 30,
        maxread: int = 2000,
        searchwindowsize: int | None = None,
        logfile: _SupportsWriteFlush[str] | None = None,
        cwd: StrOrBytesPath | None = None,
        env: subprocess._ENV | None = None,
        *,
        encoding: str,
        codec_errors: str = "strict",
        preexec_fn: Callable[[], object] | None = None,
    ) -> None: ...
    def read_nonblocking(self, size: int, timeout: float | None) -> AnyStr: ...  # type: ignore[override]
    def write(self, s: AnyStr | str) -> None: ...
    def writelines(self, sequence: Iterable[AnyStr | str]) -> None: ...
    def send(self, s: AnyStr | str) -> int: ...
    def sendline(self, s: AnyStr | str = ""): ...
    def wait(self) -> int: ...
    def kill(self, sig) -> None: ...
    def sendeof(self) -> None: ...
