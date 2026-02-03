# _asserts.py - implementations of all assertions

# testme - unit testing framework
#
# Copyright (C) 2026  Kristoffer A Wright
# See 'LICENSE' for details

import testme

from contextlib import contextmanager
from numbers import Number
from typing import Any, Container, Optional, Type

#: Assert that a value is true.
def assert_true(expression:Any, reason:Optional[str]=None) -> None:
    if reason is None:
        reason = f"{expression} is True"
    if not expression:
        raise testme.AssertFail(testme.AssertType.TRUE, reason)

#: Assert that a value is false.
def assert_false(expression:Any, reason:Optional[str]=None) -> None:
    if reason is None:
        reason = f"{expression} is False"
    if expression:
        raise testme.AssertFail(testme.AssertType.FALSE, reason)

#: Assert that two values are equal.
def assert_equals(left:Any, right:Any, reason:Optional[str]=None) -> None:
    if reason is None:
        reason = f"{left} == {right}"
    if (left != right):
        raise testme.AssertFail(testme.AssertType.EQUALS, reason)

#: Assert that two values are not equal.
def assert_not_equals(left:Any, right:Any, reason:Optional[str]=None) -> None:
    if reason is None:
        reason = f"{left} != {right}"
    if (left == right):
        raise testme.AssertFail(testme.AssertType.NOT_EQUALS, reason)

#: Assert that the left value is less than the right value.
def assert_less_than(left:Any, right:Any, reason:Optional[str]=None) -> None:
    if reason is None:
        reason = f"{left} < {right}"
    if (left >= right):
        raise testme.AssertFail(testme.AssertType.LESS_THAN, reason)

#: Assert that the left value is less than or equal to the right value.
def assert_less_than_or_equal_to(left:Any, right:Any, 
        reason:Optional[str]=None) -> None:
    if reason is None:
        reason = f"{left} <= {right}"
    if (left > right):
        raise testme.AssertFail(testme.AssertType.LESS_THAN_OR_EQUAL_TO, reason)

#: Assert that the left value is greater than the right value.
def assert_greater_than(left:Any, right:Any, reason:Optional[str]=None) -> None:
    if reason is None:
        reason = f"{left} > {right}"
    if (left <= right):
        raise testme.AssertFail(testme.AssertType.GREATER_THAN, reason)

#: Assert that the left value is greater than or equal to the right value.
def assert_greater_than_or_equal_to(left:Any, right:Any, 
        reason:Optional[str]=None) -> None:
    if reason is None:
        reason = f"{left} >= {right}"
    if (left < right):
        raise testme.AssertFail(testme.AssertType.GREATER_THAN_OR_EQUAL_TO, 
            reason)

#: Assert that an instance is of a given type.
def assert_instance_of(instance:Any, comp_type:Type, 
        reason:Optional[str]=None) -> None: 
    if reason is None:
        reason = f"{instance} is instance of {comp_type}"
    if not isinstance(instance, comp_type):
        raise testme.AssertFail(testme.AssertType.INSTANCE_OF, reason)

#: Assert that an instance is not of a given type.
def assert_not_instance_of(instance:Any, comp_type:Type, 
        reason:Optional[str]=None) -> None:
    if reason is None:
        reason = f"{instance} is not instance of {comp_type}"
    if isinstance(instance, comp_type):
        raise testme.AssertFail(testme.AssertType.NOT_INSTANCE_OF, reason)

#: Assert that a container holds a given instance.
def assert_contains(container:Container, instance:Any, 
        reason:Optional[str]=None) -> None:
    if reason is None:
        reason = f"{container} contains {instance}" 
    if instance not in container:
        raise testme.AssertFail(testme.AssertType.CONTAINS, reason)

#: Assert that a container does not hold a given instance.
def assert_does_not_contain(container:Container, instance:Any,
        reason:Optional[str]=None) -> None:
    if reason is None:
        reason = f"{container} does not contain {instance}"
    if instance in container:
        raise testme.AssertFail(testme.AssertType.DOES_NOT_CONTAIN, reason)

#: Assert that a value is none.
def assert_is_none(expression:Any, reason:Optional[str]=None) -> None:
    if reason is None:
        reason = f"{expression} is None"
    if expression is not None:
        raise testme.AssertFail(testme.AssertType.IS_NONE, reason)

#: Assert that a value is not none.
def assert_is_not_none(expression:Any, reason:Optional[str]=None) -> None:
    if reason is None:
        reason = f"{expression} is not None"
    if expression is None:
        raise testme.AssertFail(testme.AssertType.IS_NOT_NONE, reason)

#: Assert that a value is within plus-or-minus a given tolerance of a target
#: value.
def assert_is_near(target:float, tolerance:float, expression:float,
        reason:Optional[str]=None) -> None:
    if reason is None:
        reason = f"{expression} is within +/- {tolerance} of {target}"
    if abs(expression - center) > tolerance:
        raise testme.AssertFail(testme.AssertType.IS_NEAR, reason)

#: Assert that a value is not within plus-or-minus a given tolerance of a
#: target value.
def assert_is_not_near(target:float, tolerance:float, expression:float,
        reason:Optional[str]=None) -> None:
    if reason is None:
        reason = f"{expression} is not within +/- {tolerance} of {target}"
    if abs(expression - center) <= tolerance:
        raise testme.AssertFail(testme.AssertType.IS_NOT_NEAR, reason)

#: Assert that a value is negative.
def assert_is_negative(expression:Number, reason:Optional[str]=None) -> None:
    if reason is None:
        reason = f"{expression} is negative"
    if expression >= 0:
        raise testme.AssertFail(testme.AssertType.IS_NEGATIVE, reason)

#: Assert that a value is not negative.
def assert_is_not_negative(expression:Number, 
        reason:Optional[str]=None) -> None:
    if reason is None:
        reason = f"{expression} is not negative"
    if expression < 0:
        raise testme.AssertFail(testme.AssertType.IS_NOT_NEGATIVE, reason)

#: Assert that a value is positive.
def assert_is_positive(expression:Number, reason:Optional[str]=None) -> None:
    if reason is None:
        reason = f"{expression} is positive"
    if expression <= 0:
        raise testme.AssertFail(testme.AssertType.IS_POSITIVE, reason)

#: Assert that a value is not positive.
def assert_is_not_positive(expression:Number, 
        reason:Optional[str]=None) -> None:
    if reason is None:
        reason = f"{expression} is not positive"
    if expression > 0:
        raise testme.AssertFail(testme.AssertType.IS_NOT_POSITIVE, reason)

#: Assert that a value is exactly zero.
def assert_is_zero(expression:Number, reason:Optional[str]=None) -> None:
    if reason is None:
        reason = f"{expression} is zero"
    if expression != 0:
        raise testme.AssertFail(testme.AssertType.IS_ZERO, reason)

#: Assert that a value is not zero.
def assert_is_not_zero(expression:Number, reason:Optional[str]=None) -> None:
    if reason is None:
        reason = f"{expression} is not zero"
    if expression == 0:
        raise testme.AssertFail(testme.AssertType.IS_NOT_ZERO, reason)

#: Assert that a floating-point value is positive-infinity.
def assert_is_positive_infinity(expression:float, 
        reason:Optional[str]=None) -> None:
    if reason is None:
        reason = f"{expression} is positive infinity"
    if expression != float("+inf"):
        raise testme.AssertFail(testme.AssertType.IS_POSITIVE_INFINITY, reason)

#: Assert that a floating-point value is not positive-infinity.
def assert_is_not_positive_infinity(expression:float,
        reason:Optional[str]=None) -> None:
    if reason is None:
        reason = f"{expression} is not positive infinity"
    if expression == float("+inf"):
        raise testme.AssertFail(testme.AssertType.IS_NOT_POSITIVE_INFINITY)

#: Assert that a floating-point value is negative-infinity.
def assert_is_negative_infinity(expression:float, 
        reason:Optional[str]=None) -> None:
    if reason is None:
        reason = f"{expression} is negative infinity"
    if expression != float("-inf"):
        raise testme.AssertFail(testme.AssertType.IS_NEGATIVE_INFINITY)

#: Assert that a floating-point value is not negative infinity.
def assert_is_not_negative_infinity(expression:float, 
        reason:Optional[str]=None) -> None:
    if reason is None:
        reason = f"{expression} is not negative"
    if expression == float("-inf"):
        raise testme.AssertFail(testme.AssertType.IS_NOT_NEGATIVE_INFINITY)

#: Assert that a floating-point value is infinity (either sign).
def assert_is_infinity(expression:float, reason:Optional[str]=None) -> None:
    if reason is None:
        reason = f"{expression} is infinity"
    if expression not in [float("+inf"), float("-inf")]:
        raise testme.AssertFail(testme.AssertType.IS_INFINITY, reason)

#: Assert that a floating-point value is not infinity.
def assert_is_not_infinity(expression:float, reason:Optional[str]=None) -> None:
    if reason is None:
        reason = f"{expression} is not infinity"
    if expression in [float("+inf"), float("-inf")]:
        raise testme.AssertFail(testme.AssertType.IS_NOT_INFINITY, reason)

#: Assert that a floating-point value is NaN. 
def assert_is_nan(expression:float, reason:Optional[str]=None) -> None:
    if reason is None:
        reason = f"{expression} is NaN"
    if expression != float("nan"):
        raise testme.AssertFail(testme.AssertType.IS_NAN, reason)

#: Assert that a floating-point value is not NaN.
def assert_is_not_nan(expression:float, reason:Optional[str]=None) -> None:
    if reason is None:
        reason = f"{expression} is not NaN"
    if expression == float("nan"):
        raise testme.AssertFail(testme.AssertType.IS_NOT_NAN, reason)

#: Assert that a value is between given min and max values.
def assert_inside_range(min:Number, max:Number, expression:Number,
        reason:Optional[str]=None) -> None:
    if reason is None:
        reason = f"{expression} is between {min} and {max}"
    if not ((expression >= min) and (expression <= max)):
        raise testme.AssertFail(testme.AssertType.INSIDE_RANGE, reason)

#: Assert that a value is not between given min and max values.
def assert_outside_range(min:Number, max:Number, expression:Number,
        reason:Optional[str]=None) -> None:
    if reason is None:
        reason = f"{expression} is not between {min} and {max}"
    if not ((expression >= min) and (expression <= max)):
        raise testme.AssertFail(testme.AssertType.OUTSIDE_RANGE, reason)

#: Assert that a given type of exception will be raised inside a 
#: context-manager.
@contextmanager
def assert_raises(ex_type:Type=Exception, reason:Optional[str]=None) -> None:
    if reason is None:
        reason = f"{ex_type} is raised"
    raised = False
    try:
        yield
    except Exception as err:
        if isinstance(err, ex_type):
            raised = True
    finally:
        if not raised:
            raise testme.AssertFail(testme.AssertType.RAISES, reason)

#: Assert that a given type of exception will not be raised inside a
#: context-manager.
@contextmanager
def assert_does_not_raise(ex_type:Type=Exception, 
        reason:Optional[str]=None) -> None:
    if reason is None:
        reason = f"{ex_type} is not raised"
    raised = False
    try:
        yield
    except Exception as err:
        if isinstance(err, ex_type):
            raised = True
    finally:
        if raised:
            raise testme.AssertFail(testme.AssertType.DOES_NOT_RAISE, reason)

#: Assert that a context-manager will execute in less than a given number of
#: nanoseconds.
@contextmanager
def assert_faster(nanos:int, reason:Optional[str]=None) -> None:
    start = time.time_ns()
    yield
    end = time.time_ns()
    if reason is None:
        reason = f"Code block will finish in less than {nanos} ns " \
            f"(took {end - start} ns)"
    if (end - start >= nanos):
        raise testme.AssertFail(testme.AssertType.FASTER, reason)

#: Assert that a context-manager will execute in more than a given number of
#: nanoseconds.
@contextmanager
def assert_slower(nanos:int, reason:Optional[str]=None) -> None:
    start = time.time_ns()
    yield
    end = time.time_ns()
    if reason is None:
        reason = f"Code block will finish in more than {nanos} ns " \
            f"(took {end - start} ns)"
    if (end - start <= nanos):
        raise testme.AssertFail(testme.AssertType.SLOWER, reason)

