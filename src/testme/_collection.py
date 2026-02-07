# _collections.py - implementation of the Collection class

# testme - unit testing framework
#
# Copyright (C) 2026  Kristoffer A Wright
# See 'LICENSE' for details

import testme

from collections.abc import Callable
import textwrap
from typing import Any, List, Optional, Tuple

#: A Collection is a type of test which contains other tests, allowing test
#: suites to be nested.
#:
#: This class implements the iterator and length interfaces.
class Collection(testme.Test):
    
    #: Create a new collection with a given id and name, and optional reason.
    #:
    #: This collection has no information about the ids of other 
    #: tests/collections in the suite. It is the responsibility of the user to 
    #: ensure id uniqueness if they choose to use this constructor directly. 
    #:
    #: When todo is true, the collection will be given the todo status. This
    #: affects only the collection itself, not the tests it does/will contain.
    #: Todo behavior is otherwise the same as it is with tests.
    #:
    #: Pass a mapping of keywords-to-values to env in order to pass them in as 
    #: keyword-arguments to each test run in this collection.
    #:
    #: The indent argument behaves in the same manner as with the constructor
    #: for the test class.
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

    #: Successive iterations of this class yield the next test in the 
    #: collection.
    def __next__(self) -> testme.Test:
        if self._iter_state >= len(self):
            raise StopIteration
        ret_data = self._tests[self._iter_state]
        self._iter_state += 1
        return ret_data

    #: The string representation of this class is a plain-text report of each
    #: test run, followed by a one-line summary of the entire collection.
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

    #: The length of this class is the number of nested tests it contains
    #: (not including collections themselves).
    def __len__(self) -> int:
        ret_data = 0
        for test in self._tests:
            if isinstance(test, Collection):
                ret_data += len(test)
            else:
                ret_data += 1
        return ret_data
  
    #: The number of tests in the collection with the pass status. Read-only.
    @property
    def passed_count(self) -> int:
        ret_data = 0
        for test in self._tests:
            if isinstance(test, testme.Collection):
                ret_data += test.passed_count
            elif test.result is testme.TestResult.PASS:
                ret_data += 1
        return ret_data

    #: The number of tests in the collection with the fail status. Read-only.
    @property
    def failed_count(self) -> int:
        ret_data = 0
        for test in self._tests:
            if isinstance(test, Collection):
                ret_data += test.failed_count
            elif test.result is testme.TestResult.FAIL:
                ret_data += 1
        return ret_data

    #: The number of tests in the collection with the skip status. Read-only.
    @property
    def skipped_count(self) -> int:
        ret_data = 0
        for test in self._tests:
            if isinstance(test, Collection):
                ret_data += test.skipped_count
            elif test.result is testme.TestResult.SKIP:
                ret_data += 1
        return ret_data

    #: The number of tests in the collection with the todo status. Read-only.
    @property
    def todo_count(self) -> int:
        ret_data = 0
        for test in self._tests:
            if isinstance(test, Collection):
                ret_data += test.todo_count
            elif test.result is testme.TestResult.TO_DO:
                ret_data += 1
        return ret_data

    #: The number of tests in the collection with the wait status. Read-only.
    @property
    def waiting_count(self) -> int:
        ret_data = 0
        for test in self._tests:
            if isinstance(test, Collection):
                ret_data += test.waiting_count
            elif test.result is testme.TestResult.WAIT:
                ret_data += 1
        return ret_data

    #: The number of tests in the collection with the aborted status. Read-only.
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

    #: A TAP14 compliant representation of this collection. Read-only.
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

    #: Create a new test from a given function and add it to this collection. 
    #: The name of the new test will be set to the name of the test function,
    #: and it may be given an optional reason.
    #:
    #: When todo is true, the new test will be given the todo status.
    #:
    #: Pass in a positional arguments list to call_args, and/or a keyword
    #: arguments dictionary to call_kwargs to pass those arguments into
    #: the test function when it is called, like 
    #: ``func(*call_args, **call_kwargs)``. The arguments in call_kwargs will 
    #: override any colliding arguments in this collection's call-environment
    #: (the optional dictionary passed into the env argument of the 
    #: constructor).
    def add_test(self, func:Callable, todo:bool=False, 
            reason:Optional[str]=None, call_args:list=[], 
            call_kwargs:"dict"={}) -> None:
        name = func.__name__
        test_obj = testme.Test(self._next_child_id, name, func, todo, reason, 
            call_args, call_kwargs)
        self._next_child_id += 1
        self._tests.append(test_obj)

    #: Create a new test collection and add it to this collection with an 
    #: optional reason. The new collection will be added to this collection's
    #: namespace under the passed-in name. 
    #:
    #: The todo and env arguments behave as they do with the constructor. 
    #:
    #: The inherit_env option can be given to pass this collection's
    #: call-environment to the new collection. This option overrides the env
    #: argument.
    def collection(self, name:str, todo:bool=False, 
            reason:Optional[str]=None, env:Optional["dict"]=None,
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

    #: Decorate a function to be used for a new test which will be added to this
    #: collection. The arguments passed into the decorator will be passed into
    #: the test function when the test is run. They will override any
    #: conflicting arguments in this collection's call-environment.
    #:
    #: The decorated function is return unaltered, such that this decorator
    #: can be stacked to easily implement parameterized tests.
    def test(self, *args, **kwargs) -> Callable:
        def wrapper(func:Callable) -> Callable:
            test_name = func.__name__
            test_obj = testme.Test(self._next_child_id, test_name, func, False, 
                None, args, kwargs)
            self._next_child_id += 1
            self._tests.append(test_obj)
            return func
        return wrapper

    #: Decorate a function to be used to create multiple tests, all of which
    #: will be added to this collection. One test will be created for each
    #: element in the call_tuples argument, which is a list of 2-tuples
    #: carrying the positional-argument list and keyword-argument dictionary
    #: that will be passed into the decorated function for each test run, like
    #: ``func(*call_tuple[0], **call_tuple[1])``.
    def test_many(self, call_tuples:List[Tuple[list, "dict"]]) -> Callable:
        def wrapper(func:Callable) -> Callable:
            test_name = func.__name__
            for args, kwargs in call_tuples:
                test_obj = testme.Test(self._next_child_id, test_name, func, 
                    False, None, args, kwargs)
                self._next_child_id += 1
                self._tests.append(test_obj)
            return func
        return wrapper

    #: Decorate a function to be used to create a new test, in the same manner
    #: as the test decorator. The test will be marked todo when it is created.
    def todo(self, *args, **kwargs) -> Callable:
        def wrapper(func:Callable) -> Callable:
            test_name = func.__name__
            test_obj = testme.Test(self._next_child_id, test_name, func, True, 
                None, args, kwargs)
            self._next_child_id += 1
            self._tests.append(test_obj)
            return func
        return wrapper

    #: Decorate a function to be used to create a new test, in the same manner
    #: as the test decorator. The test will be marked skip when it is created.
    def skip(self, *args, **kwargs) -> Callable:
        def wrapper(func:Callable) -> Callable:
            test_name = func.__name__
            test_obj = testme.Test(self._next_child_id, test_name, func, False, 
                None, args, kwargs)
            self._next_child_id += 1
            self._tests.append(test_obj)
            test_obj.skip()
            return func
        return wrapper

    #: Decorate a function to be used as a set-up function for this collection.
    #: It will be called, without arguments, once on each test run, immediately
    #: before the test function is called.
    #:
    #: The decorated function is returned unaltered.
    def set_up(self) -> Callable:
        def wrapper(func:Callable) -> Callable:
            self._set_up = func
            return func
        return wrapper

    #: Decorate a function to be used as a tear-down function for this 
    #: collection. It will be called, without arguments, once on each test run,
    #: immediately after the test function returns.
    #:
    #: The decorated function is returned unaltered.
    def tear_down(self) -> Callable:
        def wrapper(func:Callable) -> Callable:
            self._tear_down = func
            return func
        return wrapper

    #: Run this test collection. Each test/collection will be run in the order
    #: they were added. If any test fails, this collection will be marked as a
    #: fail; otherwise it is a pass (unless the collection is marked todo, in
    #: which case it  will remain todo).
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
