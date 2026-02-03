# _collections.py - implementation of the Collection class

# testme - unit testing framework
#
# Copyright (C) 2026  Kristoffer A Wright
# See 'LICENSE' for details

import testme

from collections.abc import Callable
imoprt textwrap
from typing import Any, Optional, Tuple

class Collection(testme.Test):
    
    def __init__(self, id:int, name:str, todo:bool=False, 
            reason:Optional[str]=None, env:Optional[dict]=None,
            indent:int=4) -> None:
        super().__init__(id, name, None, todo, reason, indent=indent)
        self._iter_state = 0
        self._tests = []
        self._next_child_id = 1
        self._set_up = None
        self._tear_down = None
        self._env = env
        
    def __iter__(self) -> "Collection":
        return self

    def __next__(self) -> testme.Test:
        if self._iter_state >= len(self):
            raise StopIteration
        ret_data = self._tests[self._iter_state]
        self._iter_state += 1
        return ret_data

    def __repr__(self) -> str:
        ret_data = f"{super().__repr__()}\n"
        for test in self._tests:
            ret_data += textwrap.indent(f"{test}\n", " " * self._indent)
        ret_data += f"<<{self.passed_count} passed, "
        ret_data += f"{self.failed_count} failed, "
        ret_data += f"{self.waiting_count} waiting, "
        ret_data += f"{self.skipped_count} skipped, "
        ret_data += f"{self.todo_count} todo, "
        ret_data += f"{self.aborted_count} aborted, "
        ret_data += f"{len(self)} TOTAL>>\n"
        return ret_data

    def __len__(self) -> int:
        ret_data = 0
        for test in self._tests:
            if isinstance(test, Collection):
                ret_data += len(test)
            else:
                ret_data += 1
        return ret_data
   
    @property
    def passed_count(self) -> int:
        ret_data = 0
        for test in self._tests:
            if isinstance(test, testme.Collection):
                ret_data += test.passed_count
            elif test.result is testme.TestResult.PASS:
                ret_data += 1
        return ret_data

    @property
    def failed_count(self) -> int:
        ret_data = 0
        for test in self._tests:
            if isinstance(test, Collection):
                ret_data += test.failed_count
            elif test.result is testme.TestResult.FAIL:
                ret_data += 1
        return ret_data

    @property
    def skipped_count(self) -> int:
        ret_data = 0
        for test in self._tests:
            if isinstance(test, Collection):
                ret_data += test.skipped_count
            elif test.result is testme.TestResult.SKIP:
                ret_data += 1
        return ret_data

    @property
    def todo_count(self) -> int:
        ret_data = 0
        for test in self._tests:
            if isinstance(test, Collection):
                ret_data += test.todo_count
            elif test.result is testme.TestResult.TO_DO:
                ret_data += 1
        return ret_data

    @property
    def waiting_count(self) -> int:
        ret_data = 0
        for test in self._tests:
            if isinstance(test, Collection):
                ret_data += test.waiting_count
            elif test.result is testme.TestResult.WAIT:
                ret_data += 1
        return ret_data

    @property
    def aborted_count(self) -> int:
        ret_data = 0
        for test in self._tests:
            if isinstance(test, Collection):
                ret_data += test.aborted_count
            elif test.result is testme.TestResult.ABRT:
                ret_data += 1
        return ret_data

    @property
    def dict(self) -> str:
        ret_data = super().dict
        subtests = []
        for test in self._tests:
            subtests.append(test.dict)
        ret_data["subtests"] = {
            "tests": subtests,
            "passed_count": self.passed_count,
            "failed_count": self.failed_count,
            "waiting_count": self.waiting_count,
            "skipped_count": self.skipped_count,
            "todo_count": self.todo_count,
            "total": len(self)
        }
        return ret_data

    @property
    def tap(self) -> str:
        ret_data = f"# Subtest: {self.name}()\n"
        ret_data += f"    1..{len(self._tests)}\n"
        for test in self._tests:
            if test.result is testme.TestResult.ABRT:
                ret_data += f"{test.tap}"
                return ret_data
            ret_data += f"    {test.tap}\n"
        temp_reason = self._reason
        temp_args = self._call_args
        temp_kwargs = self._call_kwargs
        temp_residue = self._residue
        self._reason = None                     # Hide anthing that will
        self._call_args = []                    # adorn the bottom test-point
        self._call_kwargs = {}                  # output; the name needs to
        self._residue = None                    # match the comment above the
        ret_data += super().tap                 # start of the subtest...
        self._reason = temp_reason
        self._call_args = temp_args
        self._call_kwargs = temp_kwargs
        self._residue = temp_residue
        return ret_data

    def add_test(self, func:Callable, todo:bool=False, 
            reason:Optional[str]=None, call_args:list=[], 
            call_kwargs:dict={}) -> None:
        name = func.__name__
        test_obj = testme.Test(self._next_child_id, name, func, todo, reason, 
            call_args, call_kwargs)
        self._next_child_id += 1
        self._tests.append(test_obj)

    def collection(self, name:str, todo:bool=False, 
            reason:Optional[str]=None, env:Optional[dict]=None,
            inherit_env:bool=False) -> None:
        if inherit_env:
            collection_obj = Collection(self._next_child_id, name, todo, reason,
                self._env, indent=self._indent)
        else:
            collection_obj = Collection(self._next_child_id, name, todo, reason,
                env, indent=self._indent)
        self._next_child_id += 1
        self._tests.append(collection_obj)
        setattr(self, name, collection_obj)

    def test(self, *args, **kwargs) -> Callable:
        def wrapper(func:Callable) -> Callable:
            test_name = func.__name__
            test_obj = testme.Test(self._next_child_id, test_name, func, False, 
                None, args, kwargs)
            self._next_child_id += 1
            self._tests.append(test_obj)
            return func
        return wrapper

    def test_many(self, call_tuples:List[Tuple[list, dict]]) -> Callable:
        def wrapper(func:Callable) -> Callable:
            test_name = func.__name__
            for args, kwargs in call_tuples:
                test_obj = testme.Test(self._next_child_id, test_name, func, 
                    False, None, args, kwargs)
                self._next_child_id += 1
                self._tests.append(test_obj)
            return func
        return wrapper

    def todo(self, *args, **kwargs) -> Callable:
        def wrapper(func:Callable) -> Callable:
            test_name = func.__name__
            test_obj = testme.Test(self._next_child_id, test_name, func, True, 
                None, args, kwargs)
            self._next_child_id += 1
            self._tests.append(test_obj)
            return func
        return wrapper

    def skip(self, *args, **kwargs) -> Callable:
        def wrapper(func:Callable) -> Callable:
            test_name = func.__name__
            test_obj = testme.Test(self._next_child_id, test_name, func, False, 
                None, args, kwargs)
            self._next_child_id += 1
            self._tests.append(test_obj)
            test_obj.skip(reason)
            return func
        return wrapper

    def set_up(self) -> Callable:
        def wrapper(func:Callable) -> Callable:
            self._set_up = func
            return func
        return wrapper

    def tear_down(self) -> Callable:
        def wrapper(func:Callable) -> Callable:
            self._tear_down = func
            return func
        return wrapper

    def run(self) -> testme.TestResult:
        if self._ran:
            raise RuntimeError("Test collection already run")
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
                self._result = testme.TestResult.ABRT
                self._reason = f"TESTING ABORTED{err}"
                self._ran = True
                self._passed = False
                raise err
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
