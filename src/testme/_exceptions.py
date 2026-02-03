# _exceptions.py - implementations of all exceptions

# testme - unit testing framework
#
# Copyright (C) 2026  Kristoffer A Wright
# See 'LICENSE' for details

import testme

from typing import Optional

#: Raised by ``testme.assert_*`` functions to signal the controlled failure of
#: a test.
class AssertFail(Exception):

    #: Create a new instance of this class where assert_type indicates the type
    #: of assertion that failed.
    def __init__(self, assert_type:testme.AssertType, reason:str) -> None:
        self._reason = reason
        super().__init__(reason)
        self._assert_type = assert_type

    #: The string representation of this class includes is assertion type and
    #: reason.
    def __repr__(self) -> str:
        return f"Failed ASSERT_{self.assert_type.value.upper()}: " \
            f"{self.reason}"

    def __str__(self) -> str:
        return self.__repr__()

    #: The reason why this assertion failed.
    @property
    def reason(self) -> Optional[str]:
        return self._reason

    #: The type of assertion that failed.
    @property
    def assert_type(self) -> testme.AssertType:
        return self._assert_type

#: Raised by the user to force immediate termination of testing.
class Abort(Exception):
   
    #: Create a new instance of this class with an optional reason.
    def __init__(self, reason:Optional[str] = None) -> None:
        self._reason = reason
        if self._reason is None:
            super().__init__()
        else:
            super().__init__(reason)

    #: The string representation of this class includes the reason.
    def __repr__(self) -> str:
        if self._reason is None:
            return ""
        else:
            return f" - {self._reason}"

    def __str__(self) -> str:
        return self.__repr__()

