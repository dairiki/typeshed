import io
import re
import subprocess
from _typeshed import Incomplete, StrOrBytesPath
from collections.abc import Iterable, Sequence
from typing import AnyStr, Literal, overload

from pexpect import ExceptionPexpect

from .pty_spawn import spawn
from .spawnbase import _BufferType, _SupportsWriteFlush

class ExceptionPxssh(ExceptionPexpect): ...

class pxssh(spawn[AnyStr, _BufferType]):
    name: str
    UNIQUE_PROMPT: str
    PROMPT: Incomplete
    PROMPT_SET_SH: str
    PROMPT_SET_CSH: str
    SSH_OPTS: Incomplete
    force_password: bool
    debug_command_string: Incomplete
    options: Incomplete
    @overload
    def __init__(
        self: pxssh[bytes, io.BytesIO],
        timeout: float | None = 30,
        maxread: int = 2000,
        searchwindowsize: int | None = None,
        logfile: _SupportsWriteFlush[bytes] | None = None,
        cwd: StrOrBytesPath | None = None,
        env: subprocess._ENV | None = None,
        ignore_sighup: bool = False,
        echo: bool = True,
        options: dict[str, Incomplete] = {},
        encoding: None = None,
        codec_errors: str = "strict",
        debug_command_string: bool = False,
        use_poll: bool = False,
    ) -> None: ...
    @overload
    def __init__(
        self: pxssh[str, io.StringIO],
        timeout: float | None = 30,
        maxread: int = 2000,
        searchwindowsize: int | None = None,
        logfile: _SupportsWriteFlush[str] | None = None,
        cwd: StrOrBytesPath | None = None,
        env: subprocess._ENV | None = None,
        ignore_sighup: bool = False,
        echo: bool = True,
        options: dict[str, Incomplete] = {},
        *,
        encoding: str,
        codec_errors: str = "strict",
        debug_command_string: bool = False,
        use_poll: bool = False,
    ) -> None: ...
    @overload
    def __init__(
        self: pxssh[str, io.StringIO],
        timeout: float | None,
        maxread: int,
        searchwindowsize: int | None,
        logfile: _SupportsWriteFlush[str] | None,
        cwd: StrOrBytesPath | None,
        env: subprocess._ENV | None,
        ignore_sighup: bool,
        echo: bool,
        options: dict[str, Incomplete],
        encoding: str,
        codec_errors: str = "strict",
        debug_command_string: bool = False,
        use_poll: bool = False,
    ) -> None: ...
    def levenshtein_distance(self, a: Sequence[object], b: Sequence[object]) -> int: ...
    def try_read_prompt(self, timeout_multiplier: float) -> AnyStr: ...
    def sync_original_prompt(self, sync_multiplier: float = 1.0) -> bool: ...
    def login(
        self,
        server: str,
        username: str | None = None,
        password: str = "",
        terminal_type: str = "ansi",
        original_prompt: str | re.Pattern[str] = "[#$]",
        login_timeout: float | None = 10,
        port: int | None = None,
        auto_prompt_reset: bool = True,
        ssh_key: StrOrBytesPath | Literal[True] | None = None,
        quiet: bool = True,
        sync_multiplier: float = 1,
        check_local_ip: bool = True,
        password_regex: str | re.Pattern[str] = "(?i)(?:password:)|(?:passphrase for key)",
        ssh_tunnels: dict[Literal["local", "remote", "dynamic"], Iterable[str]] = {},
        spawn_local_ssh: bool = True,
        sync_original_prompt: bool = True,
        ssh_config: str | None = None,
        cmd: str = "ssh",
    ) -> Literal[True] | str: ...
    def logout(self) -> None: ...
    def prompt(self, timeout: float | None = -1) -> bool: ...
    def set_unique_prompt(self) -> bool: ...
