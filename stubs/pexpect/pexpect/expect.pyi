import re
from _typeshed import Incomplete
from collections.abc import Iterable
from typing import AnyStr, Generic

from .spawnbase import SpawnBase, _CompiledPattern

class searcher_string(Generic[AnyStr]):
    eof_index: int
    timeout_index: int
    longest_string: int
    def __init__(self, strings: Iterable[AnyStr]) -> None: ...
    match: AnyStr
    start: int
    end: int
    def search(self, buffer: AnyStr, freshlen, searchwindowsize: int | None = None) -> int: ...

class searcher_re(Generic[AnyStr]):
    eof_index: int
    timeout_index: int
    def __init__(self, patterns: Iterable[_CompiledPattern[AnyStr]]) -> None: ...
    start: int
    end: int
    match: re.Match[AnyStr]
    def search(self, buffer: AnyStr, freshlen: int, searchwindowsize: int | None = None) -> int: ...

class Expecter(Generic[AnyStr]):
    spawn: SpawnBase[AnyStr]
    searcher: searcher_re[AnyStr] | searcher_string[AnyStr]
    searchwindowsize: int | None
    lookback: int | None
    def __init__(
        self, spawn: SpawnBase[AnyStr], searcher: searcher_re[AnyStr] | searcher_string[AnyStr], searchwindowsize: int = -1
    ) -> None: ...
    def do_search(self, window: AnyStr, freshlen: int) -> int | None: ...
    def existing_data(self) -> int | None: ...
    def new_data(self, data: AnyStr) -> int | None: ...
    def eof(self, err: Incomplete | str | None = None) -> int: ...
    def timeout(self, err: object | None = None) -> int: ...
    def errored(self) -> None: ...
    def expect_loop(self, timeout: float | None = -1) -> int: ...
