# _enums.py - implementations of all enum classes

# testme - unit testing framework
#
# Copyright (C) 2026  Kristoffer A Wright
# See 'LICENSE' for details

import enum

#: Used by the AssertFail exception to indicate which type of assertion
#: triggered the failure. Member values are the same as their name, forced to
#: lowercase.
class AssertType(enum.StrEnum):
    TRUE = enum.auto()
    FALSE = enum.auto()
    EQUALS = enum.auto()
    NOT_EQUALS = enum.auto()
    LESS_THAN = enum.auto()
    LESS_THAN_OR_EQUAL_TO = enum.auto()
    GREATER_THAN = enum.auto()
    GREATER_THAN_OR_EQUAL_TO = enum.auto()
    INSTANCE_OF = enum.auto()
    NOT_INSTANCE_OF = enum.auto()
    CONTAINS = enum.auto()
    DOES_NOT_CONTAIN = enum.auto()
    IS_NONE = enum.auto()
    IS_NOT_NONE = enum.auto()
    IS_NEAR = enum.auto()
    IS_NOT_NEAR = enum.auto()
    IS_NEGATIVE = enum.auto()
    IS_NOT_NEGATIVE = enum.auto()
    IS_POSITIVE = enum.auto()
    IS_NOT_POSITIVE = enum.auto()
    IS_ZERO = enum.auto()
    IS_NOT_ZERO = enum.auto()
    IS_POSITIVE_INFINITY = enum.auto()
    IS_NOT_POSITIVE_INFINITY = enum.auto()
    IS_NEGATIVE_INFINITY = enum.auto()
    IS_NOT_NEGATIVE_INFINITY = enum.auto()
    IS_INFINITY = enum.auto()
    IS_NOT_INFINITY = enum.auto()
    IS_NAN = enum.auto()
    IS_NOT_NAN = enum.auto()
    INSIDE_RANGE = enum.auto()
    OUTSIDE_RANGE = enum.auto()
    RAISES = enum.auto()
    DOES_NOT_RAISE = enum.auto()
    FASTER = enum.auto()
    SLOWER = enum.auto()

#: Indicates the result/status of a test run.
class TestResult(enum.StrEnum):
    PASS = enum.auto()
    FAIL = enum.auto()
    SKIP = enum.auto()
    TO_DO = "TODO"                      # Avoid tripping todo grepping scripts
    WAIT = enum.auto()
    ABRT = enum.auto()
