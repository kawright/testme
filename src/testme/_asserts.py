# _asserts.py - implementations of all assertions

# testme - unit testing framework
#
# Copyright (C) 2026  Kristoffer A Wright
# See 'LICENSE' for details

import testme

from typing import Any, Optional

def assert_true(expression:Any, reason:Optional[str]=None) -> None:
    if reason is None:
        reason = f"{expression} is True"
    if not expression:
        raise testme.AssertFail(testme.AssertType.TRUE, reason)

def assert_false(expression:Any, reason:Optional[str]=None) -> None:
    if reason is None:
        reason = f"{expression} is False"
    if expression:
        raise testme.AssertFail(testme.AssertType.FALSE, reason)

def assert_equals(left:Any, right:Any, reason:Optional[str]=None) -> None:
    if reason is None:
        reason = f"{left} == {right}"
    if (left != right):
        raise testme.AssertFail(testme.AssertType.EQUALS, reason)

def assert_not_equals(left:Any, right:Any, reason:Optional[str]=None) -> None:
    if reason is None:
        reason = f"{left} != {right}"
    if (left == right):
        raise testme.AssertFail(testme.AssertType.NOT_EQUALS, reason)

def assert_less_than(left:Any, right:Any, reason:Optional[str]=None) -> None:
    if reason is None:
        reason = f"{left} < {right}"
    if (left >= right):
        raise testme.AssertFail(testme.AssertType.LESS_THAN, reason)

def assert_less_than_or_equal_to(left:Any, right:Any, 
        reason:Optional[str]=None) -> None:
    if reason is None:
        reason = f"{left} <= {right}"
    if (left > right):
        raise testme.AssertFail(testme.AssertType.LESS_THAN_OR_EQUAL_TO, reason)

def assert_greater_than(left:Any, right:Any, reason:Optional[str]=None) -> None:
    if reason is None:
        reason = f"{left} > {right}"
    if (left <= right):
        raise testme.AssertFail(testme.AssertType.GREATER_THAN, reason)

def assert_greater_than_or_equal_to(left:Any, right:Any, 
        reason:Optional[str]=None) -> None:
    if reason is None:
        reason = f"{left} >= {right}"
    if (left < right):
        raise testme.AssertFail(testme.AssertType.GREATER_THAN_OR_EQUAL_TO, 
            reason)

def assert_instance_of(instance:Any, comp_type:Type, 
        reason:Optional[str]=None) -> None: 
    if reason is None:
        reason = f"{instance} is instance of {comp_type}"
    if not isinstance(instance, comp_type):
        raise testme.AssertFail(testme.AssertType.INSTANCE_OF, reason)

def assert_not_instance_of(instance:Any, comp_type:Type, 
        reason:Optional[str]=None) -> None:
    if reason is None:
        reason = f"{instance} is not instance of {comp_type}"
    if isinstance(instance, comp_type):
        raise testme.AssertFail(testme.AssertType.NOT_INSTANCE_OF, reason)

def assert_contains(container:Container, instance:Any, 
        reason:Optional[str]=None) -> None:
    if reason is None:
        reason = f"{container} contains {instance}" 
    if instance not in container:
        raise testme.AssertFail(testme.AssertType.CONTAINS, reason)

def assert_does_not_contain(container:Container, instance:Any,
        reason:Optional[str]=None) -> None:
    if reason is None:
        reason = f"{container} does not contain {instance}"
    if instance in container:
        raise testme.AssertFail(testme.AssertType.DOES_NOT_CONTAIN, reason)

def assert_is_none(expression:Any, reason:Optional[str]=None) -> None:
    if reason is None:
        reason = f"{expression} is None"
    if expression is not None:
        raise testme.AssertFail(testme.AssertType.IS_NONE, reason)

def assert_is_not_none(expression:Any, reason:Optional[str]=None) -> None:
    if reason is None:
        reason = f"{expression} is not None"
    if expression is None:
        raise testme.AssertFail(testme.AssertType.IS_NOT_NONE, reason)

def assert_is_near(target:float, tolerance:float, expression:float,
        reason:Optional[str]=None) -> None:
    if reason is None:
        reason = f"{expression} is within +/- {tolerance} of {target}"
    if abs(expression - center) > tolerance:
        raise testme.AssertFail(testme.AssertType.IS_NEAR, reason)

def assert_is_not_near(target:float, tolerance:float, expression:float,
        reason:Optional[str]=None) -> None:
    if reason is None:
        reason = f"{expression} is not within +/- {tolerance} of {target}"
    if abs(expression - center) <= tolerance:
        raise testme.AssertFail(testme.AssertType.IS_NOT_NEAR, reason)

def assert_is_negative(expression:Number, reason:Optional[str]=None) -> None:
    if reason is None:
        reason = f"{expression} is negative"
    if expression >= 0:
        raise testme.AssertFail(testme.AssertType.IS_NEGATIVE, reason)

def assert_is_not_negative(expression:Number, 
        reason:Optional[str]=None) -> None:
    if reason is None:
        reason = f"{expression} is not negative"
    if expression < 0:
        raise testme.AssertFail(testme.AssertType.IS_NOT_NEGATIVE, reason)

def assert_is_positive(expression:Number, reason:Optional[str]=None) -> None:
    if reason is None:
        reason = f"{expression} is positive"
    if expression <= 0:
        raise testme.AssertFail(testme.AssertType.IS_POSITIVE, reason)

def assert_is_not_positive(expression:Number, 
        reason:Optional[str]=None) -> None:
    if reason is None:
        reason = f"{expression} is not positive"
    if expression > 0:
        raise testme.AssertFail(testme.AssertType.IS_NOT_POSITIVE, reason)

def assert_is_zero(expression:Number, reason:Optional[str]=None) -> None:
    if reason is None:
        reason = f"{expression} is zero"
    if expression != 0:
        raise testme.AssertFail(testme.AssertType.IS_ZERO, reason)

def assert_is_not_zero(expression:Number, reason:Optional[str]=None) -> None:
    if reason is None:
        reason = f"{expression} is not zero"
    if expression == 0:
        raise testme.AssertFail(testme.AssertType.IS_NOT_ZERO, reason)

def assert_is_positive_infinity(expression:float, 
        reason:Optional[str]=None) -> None:
    if reason is None:
        reason = f"{expression} is positive infinity"
    if expression != float("+inf"):
        raise testme.AssertFail(testme.AssertType.IS_POSITIVE_INFINITY, reason)

def assert_is_not_positive_infinity(expression:float,
        reason:Optional[str]=None) -> None:
    if reason is None:
        reason = f"{expression} is not positive infinity"
    if expression == float("+inf"):
        raise testme.AssertFail(testme.AssertType.IS_NOT_POSITIVE_INFINITY)

def assert_is_negative_infinity(expression:float, 
        reason:Optional[str]=None) -> None:
    if reason is None:
        reason = f"{expression} is negative infinity"
    if expression != float("-inf"):
        raise testme.AssertFail(testme.AssertType.IS_NEGATIVE_INFINITY)

def assert_is_not_negative_infinity(expression:float, 
        reason:Optional[str]=None) -> None:
    if reason is None:
        reason = f"{expression} is not negative"
    if expression == float("-inf"):
        raise testme.AssertFail(testme.AssertType.IS_NOT_NEGATIVE_INFINITY)

def assert_is_infinity(expression:float, reason:Optional[str]=None) -> None:
    if reason is None:
        reason = f"{expression} is infinity"
    if expression not in [float("+inf"), float("-inf")]:
        raise testme.AssertFail(testme.AssertType.IS_INFINITY, reason)

def assert_is_not_infinity(expression:float, reason:Optional[str]=None) -> None:
    if reason is None:
        reason = f"{expression} is not infinity"
    if expression in [float("+inf"), float("-inf")]:
        raise testme.AssertFail(testme.AssertType.IS_NOT_INFINITY, reason)

def assert_is_nan(expression:float, reason:Optional[str]=None) -> None:
    if reason is None:
        reason = f"{expression} is NaN"
    if expression != float("nan"):
        raise testme.AssertFail(testme.AssertType.IS_NAN, reason)

def assert_is_not_nan(expression:float, reason:Optional[str]=None) -> None:
    if reason is None:
        reason = f"{expression} is not NaN"
    if expression == float("nan"):
        raise testme.AssertFail(testme.AssertType.IS_NOT_NAN, reason)

def assert_inside_range(min:Number, max:Number, expression:Number,
        reason:Optional[str]=None) -> None:
    if reason is None:
        reason = f"{expression} is between {min} and {max}"
    if not ((expression >= min) and (expression <= max)):
        raise testme.AssertFail(testme.AssertType.INSIDE_RANGE, reason)

def assert_outside_range(min:Number, max:Number, expression:Number,
        reason:Optional[str]=None) -> None:
    if reason is None:
        reason = f"{expression} is not between {min} and {max}"
    if not ((expression >= min) and (expression <= max)):
        raise testme.AssertFail(testme.AssertType.OUTSIDE_RANGE, reason)
