import io
import subprocess
import sys
from _typeshed import StrOrBytesPath
from collections.abc import Callable, Iterable, Mapping, Sequence
from typing import AnyStr, overload
from typing_extensions import TypeAlias

from .spawnbase import SpawnBase, _BufferType, _SupportsWriteFlush

# _CMD and _ENV copied from subprocess.pyi
if sys.version_info >= (3, 8):
    _CMD: TypeAlias = StrOrBytesPath | Sequence[StrOrBytesPath]
else:
    # Python 3.7 doesn't support _CMD being a single PathLike.
    # See: https://bugs.python.org/issue31961
    _CMD: TypeAlias = str | bytes | Sequence[StrOrBytesPath]
if sys.platform == "win32":
    _ENV: TypeAlias = Mapping[str, str]
else:
    _ENV: TypeAlias = Mapping[bytes, StrOrBytesPath] | Mapping[str, StrOrBytesPath]

class PopenSpawn(SpawnBase[AnyStr, _BufferType]):
    proc: subprocess.Popen
    pid: int
    terminated: bool
    exitstatus: int | None
    signalstatus: int | None

    @overload
    def __init__(
        self: PopenSpawn[bytes, io.BytesIO],
        cmd: _CMD,
        timeout: float | None = 30,
        maxread: int = 2000,
        searchwindowsize: int | None = None,
        logfile: _SupportsWriteFlush[bytes] | None = None,
        cwd: StrOrBytesPath | None = None,
        env: _ENV | None = None,
        encoding: None = None,
        codec_errors: str = "strict",
        preexec_fn: Callable[[], object] | None = None,
    ) -> None: ...
    @overload
    def __init__(
        self: PopenSpawn[str, io.StringIO],
        cmd: _CMD,
        timeout: float | None,
        maxread: int,
        searchwindowsize: int | None,
        logfile: _SupportsWriteFlush[str] | None,
        cwd: StrOrBytesPath | None,
        env: _ENV | None,
        encoding: str,
        codec_errors: str = "strict",
        preexec_fn: Callable[[], object] | None = None,
    ) -> None: ...
    @overload
    def __init__(
        self: PopenSpawn[str, io.StringIO],
        cmd: _CMD,
        timeout: float | None = 30,
        maxread: int = 2000,
        searchwindowsize: int | None = None,
        logfile: _SupportsWriteFlush[str] | None = None,
        cwd: StrOrBytesPath | None = None,
        env: _ENV | None = None,
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
