# _test.py - implementation of the test class

# testme - unit testing framework
#
# Copyright (C) 2026  Kristoffer A Wright
# See 'LICENSE' for details

import testme

from collections.abc import Callable
import json
from typing import Any, Optional

#: This class represents the smallest unit of concern in the testme framework:
#: a single test run. 
class Test:

    #: Create a new instance of this class with given name and id, and optional
    #: reason.
    #:
    #: This test has no information about the ids of other tests/collections
    #: in the suite. It is the responsibility of the user to ensure id
    #: uniqueness if they choose to use this constructor directly.
    #:
    #: Giving the todo option marks this test as a todo item, meaning its
    #: outcome will not affect the suite/collection that contains it. A test's
    #: result status is invariant once it is set to todo.
    #:
    #: Pass a positional-argument list to call_args, and/or a keyword-argument
    #: dict to call_kwargs to pass them to the test-function when the test
    #: is run.
    #:
    #: The indentation level for formatted representations of this object can
    #: be set with indent. This behavior is format-dependent.
    def __init__(self, id:int, name:str, test:Callable, todo:bool=False, 
            reason:Optional[str]=None, call_args:list=[],
            call_kwargs:dict={}, indent:int=4) -> None:
        self._id = id
        self._name = name
        self._test = test
        self._skipped = False
        self._ran = False
        self._exception = None
        self._passed = False
        self._result = testme.TestResult.WAIT
        self._reason = reason
        self._todo = todo
        self._call_args = call_args
        self._call_kwargs = call_kwargs
        self._residue = None
        self._indent = indent

    #: The string representation of this class is a plain-text report of this
    #: status run.
    def __repr__(self) -> str:
        if self.passed:
            pass_str = "[x]"
        else:
            pass_str = "[ ]"
        ret_data = f"{self.id}. {self.result.value.upper()} {pass_str}: " \
            f"{self.name}"
        ret_data += "("
        if (len(self._call_args) > 0) or (len(self._call_kwargs) > 0):
            for arg in self._call_args:
                ret_data += f"{arg}, "
            for kwarg in self._call_kwargs:
                ret_data += f"{kwarg}={self._call_kwargs[kwarg]}, "
            ret_data = ret_data[:-2]
        ret_data += ")"
        if self.residue is not None:
            ret_data += f" -> {self.residue}"
        if self.reason is not None:
            ret_data += f" ({self.reason})"
        return ret_data

    def __call__(self) -> bool:
        return self.run()

    #: The id of this test. Read-only.
    @property
    def id(self) -> int:
        return self._id

    #: The name of this test. Read-only.
    @property
    def name(self) -> str:
        return self._name

    #: True if this test was/will-be skipped. Read-only.
    @property
    def skipped(self) -> bool:
        return self._skipped

    #: True if this test is a todo item. Read-only.
    @property
    def todo(self) -> bool:
        return self._todo

    #: True once the test function has been called. Read-only.
    @property
    def ran(self) -> bool:
        return self._ran

    #: True if the test function was called and returned. Read-only.
    @property
    def passed(self) -> bool:
        return self._passed

    #: An optional summary of this test. Read-only.
    @property
    def reason(self) -> str:
        if not self.ran:
            return None
        return self._reason

    #: If an exception is raised while the test function executes (aside from 
    #: AssertFail or Abort), this property will contain a reference to it.
    #: Otherwise, it is none. Read-only.
    @property
    def exception(self) -> Optional[Exception]:
        return self._exception

    #: The result of this test. This will be TestResult.WAIT until the test
    #: is run. Read-only.
    @property
    def result(self) -> testme.TestResult:
        return self._result

    #: The return value of the test function. For reporting purposes. Read-only.
    @property
    def residue(self) -> Any:
        return self._residue

    #: A dictionary representation of this test. Schematically identical
    #: to the output of the json property. Read-only.
    @property
    def dict(self) -> dict:
        clean_args = []
        for arg in self._call_args:
            clean_args.append(str(arg))
        clean_kwargs = {}
        for kwarg in self._call_kwargs:
            clean_kwargs[kwarg] = str(self._call_kwargs[kwarg])
        return {
            "id": self.id,
            "name": self.name,
            "passed": self.passed,
            "result": self.result,
            "reason": self.reason,
            "positional_args": clean_args,
            "keyword_args": clean_kwargs,
            "residue": str(self.residue),
            "subtests": None
        }

    #: A json representation of this test. This instance's indent property
    #: is used to set the indentation of this value.
    @property
    def json(self) -> str:
        return json.dumps(self.dict, indent=self._indent)

    #: A TAP14 compliant test-point generated from this test.
    @property
    def tap(self) -> str:
        if self.result is testme.TestResult.ABRT:
            return f"Bail Out! {self.reason[18:]}"   # Skip "TESTING ABORTED - "
        ret_data = ""
        if not self.passed:
            ret_data += "not "
        ret_data += f"ok {self.id} - {self.name}"
        ret_data += "("
        if (len(self._call_args) > 0) or (len(self._call_kwargs) > 0):
            for arg in self._call_args:
                ret_data += f"{arg}, "
            for kwarg in self._call_kwargs:
                ret_data += f"{kwarg}={self._call_kwargs[kwarg]}, "
            ret_data = ret_data[:-2]
        ret_data += ")"
        if self.residue is not None:
            ret_data += f" -> {self.residue}"
        if self.result is testme.TestResult.TO_DO:
            ret_data += " # TODO"
            if self.reason is not None:
                ret_data += f" {self.reason}"
        elif self.result is testme.TestResult.SKIP:
            ret_data += " # SKIP"
            if self.reason is not None:
                ret_data += f" {self.reason}"
        elif self.reason is not None:
            ret_data += f" ({self.reason})"
        return ret_data

    #: Skip this test with an optional reason. The test will not be run.
    def skip(self, reason:Optional[str]=None) -> None:
        if self.ran:
            raise RuntimeException("Test already ran")
        if self.skipped:
            raise RuntimeException("Test already skipped")
        self._skipped = True
        self._reason = reason

    #: Run this test by calling the test function. If call_args or call_kwargs
    #: were given at construction, the test function will be called with them.
    #: The return value will be saved as this instance's residue property.
    #:
    #: The test will pass unless it raises an exception. If an exception is
    #: raised, it will be caught and handled as such:
    #:
    #: * If it is an instance of Abort, the result of this test will be set
    #:   to TestResult.ABRT and the exception will be reraised to eventually
    #:   be handled by the root suite object.
    #: * If it is an instance of AssertFail, the result will be set to
    #:   TestResult.FAIL. This should be considered a "formal" failure by the
    #:   user.
    #: * Otherwise the exception itself is stored as this instance's
    #:   exception property, and processing proceeds as with AssertFail. This
    #:   should be considered an unexpected failure by the user.
    #:
    #: If skip is true, the status will be updated to TestResult.SKIP and this
    #: function will immediately return without calling the test function. If
    #: todo is true, the test will be run and the outcome recorded, but the
    #: status will be set to TestResult.TO_DO without regard to said outcome.
    #:
    #: A test can only be run once. Calling for a second or subsequent times
    #: raises RuntimeError.
    #:
    #: Returns the new result property of the instance.
    def run(self) -> testme.TestResult:
        if self.ran:
            raise RuntimeError("Test already ran")
        if self.skipped:
            self._result = testme.TestResult.SKIP
            return self._result
        try:
            self._passed = True
            self._residue = self._test(*self._call_args, **self._call_kwargs)
        except Exception as err:
            if isinstance(err, Abort):
                self._result = testme.TestResult.ABRT
                self._reason = f"TESTING ABORTED{err}"
                self._ran = True
                self._passed = False
                raise err                   # Bubble Abort up to Suite
            elif isinstance(err, testme.AssertFail):
                self._passed = False
                if self._reason is None:
                    self._reason = str(err)
            else:
                self._passed = False
                self._exception = err
                if self._reason is None:
                    self._reason = str(err)
        if self._todo:
            self._result = testme.TestResult.TO_DO
        elif self._passed:
            self._result = testme.TestResult.PASS
        else:
            self._result = testme.TestResult.FAIL
        self._ran = True
        return self._result

