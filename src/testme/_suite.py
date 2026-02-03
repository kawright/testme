# _suite.py - implementation of the suite class

# testme - unit testing framework
#
# Copyright (C) 2026  Kristoffer A Wright
# See 'LICENSE' for details

import testme

from typing import Optional

#: A suite is special type of collection which represents the root of a nested
#: test collection.
class Suite(testme.Collection):

    created = False

    #: Create a new instance of this class with an optional name and reason.
    #:
    #: This is a singleton class. Attempting to create more than one will raise
    #: TypeError.
    #:
    #: If no name is given, the name of the module is used.
    #:
    #: The env and indent arguments behave in the same manner as with the
    #: constructor for the collection class.
    def __init__(self, name:Optional[str]=None, todo:bool=False, 
            reason:Optional[str]=None, env:Optional[dict]=None, 
            indent:int=4) -> None:
        if Suite.created:
            raise TypeError("Only one suite may be created")
        if name is None:
            name = __main__.__file__.split("/")[-1].split(".")[0]
        super().__init__(0, name, todo, reason, env=env, indent=indent)
        self._abort = False
        Suite.created = True

    #: The string representation of this class is a human-readable summary
    #: of the test suite.
    def __repr__(self) -> str:
        return super().__repr__()[:-1]

    #: Indicates whether or not this test-suite was aborted. Read-only.
    @property
    def abort(self) -> bool:
        return self._abort

    #: An entire TAP14 compliant document generated from this test-suite.
    @property
    def tap(self) -> str:
        ret_data = "TAP version 14\n"
        ret_data += f"1..{len(self._tests)} - {self.name}()"
        if (self.reason is not None) and \
                (self.result is not testme.TestResult.ABRT):
            ret_data += f" ({self.reason})"
        ret_data += "\n"
        for test in self._tests:
            ret_data += f"{test.tap}\n"
            if test.result is testme.TestResult.ABRT:
                return ret_data[:-1]
        return ret_data[:-1]

    #: Run this test suite. Every test and colleciton will be run recursively.
    #: Any test failure will cause the result of this test suite to be fail;
    #: otherwise it is a pass (unless the entire suite is marked todo, in
    #: which case it will remain todo).
    def run(self) -> testme.TestResult:
        if self._ran:
            raise RuntimeException("Test suite already run")
        self._passed = True
        for test in self._tests:
            if self._set_up is not None:
                self._set_up()
            if self._env is not None:
                call_kwargs = self._env.copy()
                call_kwargs.update(test._call_kwargs)
                test._call_kwargs = call_kwargs
            try:
                test()
            except Abort as err:
                self._abort = True
                self._reason = f"TESTING ABORTED{err}"
                self._result = testme.TestResult.ABRT
                self._ran = True
                self._passed = False
                return self._result
            if self._tear_down is not None:
                self._tear_down()
            if test.result is testme.TestResult.FAIL:
                self._passed = False
        if self._todo:
            self._result = testme.TestResult.TO_DO
        elif self._passed:
            self._result = testme.TestResult.PASS
        else:
            self._result = testme.TestResult.FAIL
        self._ran = True
        return self._result


