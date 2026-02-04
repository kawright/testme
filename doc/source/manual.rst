.. _reference-manual:


#######################
testme Reference Manual
#######################

This document is a complete reference manual for the *testme* library,
including all public API members. It is rather comprehensive, and may be
an overwhelming read for new users. To give these users an easier path to 
getting their feet wet with *testme*, a :ref:`quick-guide` has been provided.

****************
Package Overview
****************

The following is a complete listing of the :py:mod:`testme` source tree. API
members are listed alphabetically.

* *module* :py:mod:`testme` - root-level module
    * *function* :py:func:`testme.assert_contains` - assert a container holds
      a value
    * *function* :py:func:`testme.assert_does_not_contain` - assert a
      container does *not* hold a value
    * *function* :py:func:`testme.assert_does_not_raise` - assert a
      block of code does not raise an exception
    * *function* :py:func:`testme.assert_equals` - assert two values are
      equal
    * *function* :py:func:`testme.assert_false` - assert a value is `False`
    * *function* :py:func:`testme.assert_faster` - assert a block of code
      finishes faster than a duration
    * *function* :py:func:`testme.assert_greater_than` - assert one value
      is greater than another
    * *function* :py:func:`testme.assert_greater_than_or_equal_to` - assert
      one value is greater than or equal to another
    * *function* :py:func:`testme.assert_inside_range` - assert a value is
      between two others
    * *function* :py:func:`testme.assert_instance_of` - assert a value is of a
      type
    * *function* :py:func:`testme.assert_is_infinity` - assert a value is
      infinity
    * *function* :py:func:`testme.assert_is_nan` - assert a value is NaN
    * *function* :py:func:`testme.assert_is_near` - assert two values are near
    * *function* :py:func:`testme.assert_is_negative` - assert a value is
      negative
    * *function* :py:func:`testme.assert_is_negative_infinity` - assert a
      value is negative infinity
    * *function* :py:func:`testme.assert_is_none` - assert a value is *None* 
    * *function* :py:func:`testme.assert_is_not_nan` - assert a value is not
      NaN.
    * *function* :py:func:`testme.assert_is_not_infinity` - assert a value is
      not infinity
    * *function* :py:func:`testme.assert_is_not_near` - assert two values are
      not near
    * *function* :py:func:`testme.assert_is_not_negative` - assert a value is
      not negative.
    * *function* :py:func:`testme.assert_is_not_negative_infinity` - assert a
      value is not negative infinity
    * *function* :py:func:`testme.assert_is_not_none` - assert a value isn't
      *None*.
    * *function* :py:func:`testme.assert_is_not_positive_infinity` - assert
      a value is not positive infinity
    * *function* :py:func:`testme.assert_is_not_zero` - assert a value isn't
      zero
    * *function* :py:func:`testme.assert_is_positive` - assert a value is
      positive
    * *function* :py:func:`testme.assert_is_positive_infinity` - assert a 
      value is positive infinity
    * *function* :py:func:`testme.assert_is_zero` - assert a value is zero
    * *function* :py:func:`testme.assert_less_than` - assert one value is
      less than another
    * *function* :py:func:`testme.assert_less_than_or_equal_to` - assert one
      value is less than or equal to another
    * *function* :py:func:`testme.assert_not_equals` - assert two values are
      not equal
    * *function* :py:func:`testme.assert_not_instance_of` - assert a value
      is not of a type
    * *function* :py:func:`testme.assert_outside_range` - assert a value is
      not between two other values
    * *function* :py:func:`testme.assert_raises` - assert a block of code
      raises an exception
    * *function* :py:func:`testme.assert_slower` - assert a block of code 
      finshes slower than a duration
    * *function* :py:func:`testme.assert_true` - assert a value is `True`.
    * *exception* :py:exc:`testme.Abort` - abort an entire suite run
    * *exception* :py:exc:`testme.AssertFail` - signal a test failure
        * *attribute* :py:attr:`testme.AssertFail.assert_type`
        * *attribute* :py:attr:`testme.AssertFail.reason`
    * *enum* :py:class:`testme.AssertType` - assertion types
    * *class* :py:class:`testme.Collection` - test collections
        * *attribute* :py:attr:`testme.Collection.aborted_count`
        * *attribute* :py:attr:`testme.Collection.dict`
        * *attribute* :py:attr:`testme.Collection.failed_count`
        * *attribute* :py:attr:`testme.Collection.passed_count`
        * *attribute* :py:attr:`testme.Collection.skipped_count`
        * *attribute* :py:attr:`testme.Collection.tap`
        * *attribute* :py:attr:`testme.Collection.todo_count`
        * *attribute* :py:attr:`testme.Collection.waiting_count`
        * *method* :py:meth:`testme.Collection.__len__`
        * *method* :py:meth:`testme.Collection.__next__`
        * *method* :py:meth:`testme.Collection.__repr__`
        * *method* :py:meth:`testme.Collection.add_test` - add a test
        * *method* :py:meth:`testme.Collection.collection` - add a collection
        * *method* :py:meth:`testme.Collection.run` - run all tests 
        * *method* :py:meth:`testme.Collection.set_up` - register a set-up
          function using decorator syntax
        * *method* :py:meth:`testme.Collection.skip` - add and skip a test
          using decorator syntax
        * *method* :py:meth:`testme.Collection.tear_down` - register a
          tear-down function using decorator syntax
        * *method* :py:meth:`testme.Collection.test` - add a test using
          decorator syntax
        * *method* :py:meth:`testme.Collection.test_many` - add multiple tests
          using decorator syntax
        * *method* :py:meth:`testme.Collection.todo` - add a todo test using
          decorator syntax
    * *class* :py:class:`testme.Suite` - root collection
        * *attribute* :py:attr:`testme.Suite.abort`
        * *attribute* :py:attr:`testme.Suite.tap`
        * *method* :py:attr:`testme.Suite.__repr__`
        * *method* :py:attr:`testme.Suite.run` - run all tests
    * *class* :py:class:`testme.Test` - unit test
        * *attribute* :py:attr:`testme.Test.dict`
        * *attribute* :py:attr:`testme.Test.exception`
        * *attribute* :py:attr:`testme.Test.id`
        * *attribute* :py:attr:`testme.Test.json`
        * *attribute* :py:attr:`testme.Test.name`
        * *attribute* :py:attr:`testme.Test.passed`
        * *attribute* :py:attr:`testme.Test.ran`
        * *attribute* :py:attr:`testme.Test.reason`
        * *attribute* :py:attr:`testme.Test.residue`
        * *attribute* :py:attr:`testme.Test.result`
        * *attribute* :py:attr:`testme.Test.skipped`
        * *attribute* :py:attr:`testme.Test.tap`
        * *attribute* :py:attr:`testme.Test.todo`
        * *run* :py:meth:`testme.Test.run` - run this test
        * *method* :py:meth:`testme.Test.skip` - skip this test

*******
Modules
*******

.. py:module:: testme

*testme*
==========

.. version-added:: 0.1.0

This module contains all of the API members in the :py:mod:`testme` library.
There are no sub-modules in this module, meaning the entire package
structure is flat.

*******************
Assertion Functions
*******************

These functions are used to validate test inputs. They are the 
meat-and-potatoes of your unit-tests, and failing one of these is the only way
to "cleanly" or "formally" fail a test.

Each of them work in the same manner: they check the truth of some kind of
statement--expressed as one-or-more function arguments, but ultimately 
boiled-down to a boolean value--and raises :py:exc:`testme.AssertFail` if the 
statement proves `False`. This special exception tells :py:mod:`testme` that a 
test has failed in an expected manner, and to process it normally (see
:py:meth:`testme.Test.run` and :py:meth:`testme.Container.run` for more 
information on failure cases.

All *assert_* functions accept an optional, final keyword argument 
*reason*, which is a :py:type:`str` that explains why the assertion may have 
failed. If this is omitted, a default message will be used.

In general, each type of condition :py:mod:`testme` can check for has two
assoociated assertion functions: one which affirms it, and one which negates
it.

All assertions are listed below, and are documented in full detail.

.. autofunction:: assert_contains

    Assert that *container* contains *instance*.

.. autofunction:: assert_does_not_contain

    Assert that *container* does not contains *instance*.


