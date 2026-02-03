# _test.py - implementation of the test class

# testme - unit testing framework
#
# Copyright (C) 2026  Kristoffer A Wright
# See 'LICENSE' for details

import testme

from collections.abc import Callable
import json
from typing import Optional

class Test:

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

    @property
    def id(self) -> int:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    @property
    def skipped(self) -> bool:
        return self._skipped

    @property
    def todo(self) -> bool:
        return self._todo

    @property
    def ran(self) -> bool:
        return self._ran

    @property
    def passed(self) -> bool:
        return self._passed

    @property
    def reason(self) -> str:
        if not self.ran:
            return None
        return self._reason

    @property
    def exception(self) -> Optional[Exception]:
        return self._exception

    @property
    def result(self) -> testme.TestResult:
        return self._result

    @property
    def residue(self) -> Any:
        return self._residue

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

    @property
    def json(self) -> str:
        return json.dumps(self.dict, indent=self._indent)

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

    def skip(self, reason:Optional[str]=None) -> None:
        if self.ran:
            raise RuntimeException("Test already ran")
        if self.skipped:
            raise RuntimeException("Test already skipped")
        self._skipped = True
        self._reason = reason
        self._result = testme.TestResult.SKIP

    def run(self) -> testme.TestResult:
        if self.ran:
            raise RuntimeException("Test already ran")
        if self.skipped:
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

