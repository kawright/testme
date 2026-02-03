# _exceptions.py - implementations of all exceptions

# testme - unit testing framework
#
# Copyright (C) 2026  Kristoffer A Wright
# See 'LICENSE' for details

import testme

from typing import Optional

class AssertFail(Exception):

    def __init__(self, assert_type:testme.AssertType, reason:str) -> None:
        self._reason = reason
        super().__init__(reason)
        self._assert_type = assert_type

    def __repr__(self) -> str:
        return f"Failed ASSERT_{self.assert_type.value.upper()}: " \
            f"{self.reason}"

    def __str__(self) -> str:
        return self.__repr__()

    @property
    def reason(self) -> Optional[str]:
        return self._reason

    @property
    def assert_type(self) -> AssertType:
        return self._assert_type

class Abort(Exception):
   
    def __init__(self, reason:Optional[str] = None) -> None:
        self._reason = reason
        if self._reason is None:
            super().__init__()
        else:
            super().__init__(reason)

    def __repr__(self) -> str:
        if self._reason is None:
            return ""
        else:
            return f" - {self._reason}"

    def __str__(self) -> str:
        return self.__repr__()

