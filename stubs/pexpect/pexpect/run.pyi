import sys
from _typeshed import StrOrBytesPath
from collections.abc import Callable, Mapping, Sequence
from typing import Any, AnyStr, overload
from typing_extensions import Literal, TypeAlias

from pexpect.spawnbase import _Pattern, _SupportsWriteFlush

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

_Response: TypeAlias = AnyStr | str | Callable[[dict[str, Any]], AnyStr | str | bool | object]
_Events: TypeAlias = dict[_Pattern[AnyStr], _Response[AnyStr]] | list[tuple[_Pattern[AnyStr], _Response[AnyStr]]]

@overload
def run(
    command: _CMD,
    timeout: float | None = 30,
    withexitstatus: Literal[False] = False,
    events: _Events[bytes] | None = None,
    extra_args: object | None = None,
    logfile: _SupportsWriteFlush[bytes] | None = None,
    cwd: StrOrBytesPath | None = None,
    env: _ENV | None = None,
    *,
    encoding: None = None,
    **kwargs,
) -> bytes: ...
@overload
def run(
    command: _CMD,
    timeout: float | None = 30,
    withexitstatus: Literal[False] = False,
    events: _Events[str] | None = None,
    extra_args: object | None = None,
    logfile: _SupportsWriteFlush[str] | None = None,
    cwd: StrOrBytesPath | None = None,
    env: _ENV | None = None,
    *,
    encoding: str,
    **kwargs,
) -> str: ...
@overload
def run(
    command: _CMD,
    timeout: float | None,
    withexitstatus: Literal[True],
    events: _Events[bytes] | None = None,
    extra_args: object | None = None,
    logfile: _SupportsWriteFlush[bytes] | None = None,
    cwd: StrOrBytesPath | None = None,
    env: _ENV | None = None,
    *,
    encoding: None = None,
    **kwargs,
) -> tuple[bytes, int | None]: ...
@overload
def run(
    command: _CMD,
    timeout: float | None,
    withexitstatus: Literal[True],
    events: _Events[str] | None = None,
    extra_args: object | None = None,
    logfile: _SupportsWriteFlush[str] | None = None,
    cwd: StrOrBytesPath | None = None,
    env: _ENV | None = None,
    *,
    encoding: str,
    **kwargs,
) -> tuple[str, int | None]: ...
@overload
def run(
    command: _CMD,
    timeout: float | None = None,
    events: _Events[bytes] | None = None,
    extra_args: object | None = None,
    logfile: _SupportsWriteFlush[bytes] | None = None,
    cwd: StrOrBytesPath | None = None,
    env: _ENV | None = None,
    *,
    withexitstatus: Literal[True],
    encoding: None = None,
    **kwargs,
) -> tuple[bytes, int | None]: ...
@overload
def run(
    command: _CMD,
    timeout: float | None = None,
    events: _Events[str] | None = None,
    extra_args: object | None = None,
    logfile: _SupportsWriteFlush[str] | None = None,
    cwd: StrOrBytesPath | None = None,
    env: _ENV | None = None,
    *,
    withexitstatus: Literal[True],
    encoding: str,
    **kwargs,
) -> tuple[str, int | None]: ...
@overload
def runu(
    command: _CMD,
    timeout: float | None = 30,
    withexitstatus: Literal[False] = False,
    events: _Events[str] | None = None,
    extra_args: object | None = None,
    logfile: _SupportsWriteFlush[str] | None = None,
    cwd: StrOrBytesPath | None = None,
    env: _ENV | None = None,
    *,
    encoding: str = "utf-8",
    **kwargs,
) -> str: ...
@overload
def runu(
    command: _CMD,
    timeout: float | None,
    withexitstatus: Literal[True],
    events: _Events[str] | None = None,
    extra_args: object | None = None,
    logfile: _SupportsWriteFlush[str] | None = None,
    cwd: StrOrBytesPath | None = None,
    env: _ENV | None = None,
    *,
    encoding: str = "utf-8",
    **kwargs,
) -> tuple[str, int | None]: ...
@overload
def runu(
    command: _CMD,
    timeout: float | None = None,
    events: _Events[str] | None = None,
    extra_args: object | None = None,
    logfile: _SupportsWriteFlush[str] | None = None,
    cwd: StrOrBytesPath | None = None,
    env: _ENV | None = None,
    *,
    withexitstatus: Literal[True],
    encoding: str = "utf-8",
    **kwargs,
) -> tuple[str, int | None]: ...
