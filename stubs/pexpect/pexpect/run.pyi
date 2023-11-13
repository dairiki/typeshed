import subprocess
from _typeshed import StrOrBytesPath
from collections.abc import Callable
from typing import Any, AnyStr, overload
from typing_extensions import Literal, TypeAlias

from pexpect.spawnbase import _Pattern, _SupportsWriteFlush

_Response: TypeAlias = AnyStr | str | Callable[[dict[str, Any]], AnyStr | str | bool | object]
_Events: TypeAlias = dict[_Pattern[AnyStr], _Response[AnyStr]] | list[tuple[_Pattern[AnyStr], _Response[AnyStr]]]

@overload
def run(
    command: subprocess._CMD,
    timeout: float | None = 30,
    withexitstatus: Literal[False] = False,
    events: _Events[bytes] | None = None,
    extra_args: object | None = None,
    logfile: _SupportsWriteFlush[bytes] | None = None,
    cwd: StrOrBytesPath | None = None,
    env: subprocess._ENV | None = None,
    *,
    encoding: None = None,
    **kwargs,
) -> bytes: ...
@overload
def run(
    command: subprocess._CMD,
    timeout: float | None = 30,
    withexitstatus: Literal[False] = False,
    events: _Events[str] | None = None,
    extra_args: object | None = None,
    logfile: _SupportsWriteFlush[str] | None = None,
    cwd: StrOrBytesPath | None = None,
    env: subprocess._ENV | None = None,
    *,
    encoding: str,
    **kwargs,
) -> str: ...
@overload
def run(
    command: subprocess._CMD,
    timeout: float | None,
    withexitstatus: Literal[True],
    events: _Events[bytes] | None = None,
    extra_args: object | None = None,
    logfile: _SupportsWriteFlush[bytes] | None = None,
    cwd: StrOrBytesPath | None = None,
    env: subprocess._ENV | None = None,
    *,
    encoding: None = None,
    **kwargs,
) -> tuple[bytes, int | None]: ...
@overload
def run(
    command: subprocess._CMD,
    timeout: float | None,
    withexitstatus: Literal[True],
    events: _Events[str] | None = None,
    extra_args: object | None = None,
    logfile: _SupportsWriteFlush[str] | None = None,
    cwd: StrOrBytesPath | None = None,
    env: subprocess._ENV | None = None,
    *,
    encoding: str,
    **kwargs,
) -> tuple[str, int | None]: ...
@overload
def run(
    command: subprocess._CMD,
    timeout: float | None = None,
    events: _Events[bytes] | None = None,
    extra_args: object | None = None,
    logfile: _SupportsWriteFlush[bytes] | None = None,
    cwd: StrOrBytesPath | None = None,
    env: subprocess._ENV | None = None,
    *,
    withexitstatus: Literal[True],
    encoding: None = None,
    **kwargs,
) -> tuple[bytes, int | None]: ...
@overload
def run(
    command: subprocess._CMD,
    timeout: float | None = None,
    events: _Events[str] | None = None,
    extra_args: object | None = None,
    logfile: _SupportsWriteFlush[str] | None = None,
    cwd: StrOrBytesPath | None = None,
    env: subprocess._ENV | None = None,
    *,
    withexitstatus: Literal[True],
    encoding: str,
    **kwargs,
) -> tuple[str, int | None]: ...
@overload
def runu(
    command: subprocess._CMD,
    timeout: float | None = 30,
    withexitstatus: Literal[False] = False,
    events: _Events[str] | None = None,
    extra_args: object | None = None,
    logfile: _SupportsWriteFlush[str] | None = None,
    cwd: StrOrBytesPath | None = None,
    env: subprocess._ENV | None = None,
    *,
    encoding: str = "utf-8",
    **kwargs,
) -> str: ...
@overload
def runu(
    command: subprocess._CMD,
    timeout: float | None,
    withexitstatus: Literal[True],
    events: _Events[str] | None = None,
    extra_args: object | None = None,
    logfile: _SupportsWriteFlush[str] | None = None,
    cwd: StrOrBytesPath | None = None,
    env: subprocess._ENV | None = None,
    *,
    encoding: str = "utf-8",
    **kwargs,
) -> tuple[str, int | None]: ...
@overload
def runu(
    command: subprocess._CMD,
    timeout: float | None = None,
    events: _Events[str] | None = None,
    extra_args: object | None = None,
    logfile: _SupportsWriteFlush[str] | None = None,
    cwd: StrOrBytesPath | None = None,
    env: subprocess._ENV | None = None,
    *,
    withexitstatus: Literal[True],
    encoding: str = "utf-8",
    **kwargs,
) -> tuple[str, int | None]: ...
