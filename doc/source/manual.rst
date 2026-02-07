.. _reference-manual:


###############################
**testme** API Reference Manual
###############################

This document is a complete reference manual for the ``testme`` library,
including all public API members. It is rather comprehensive, and may be
an overwhelming read for new users. To give these users an easier path to 
getting their feet wet with ``testme``, the :ref:`quick-guide` has been 
provided.

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
    * *function* :py:func:`testme.assert_is_none` - assert a value is ``None`` 
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
      ``None``.
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
        * *property* :py:attr:`testme.AssertFail.assert_type`
        * *property* :py:attr:`testme.AssertFail.reason`
    * *enum* :py:class:`testme.AssertType` - assertion types
    * *class* :py:class:`testme.Collection` - test collections
        * *property* :py:attr:`testme.Collection.aborted_count`
        * *property* :py:attr:`testme.Collection.failed_count`
        * *property* :py:attr:`testme.Collection.passed_count`
        * *property* :py:attr:`testme.Collection.skipped_count`
        * *property* :py:attr:`testme.Collection.todo_count`
        * *property* :py:attr:`testme.Collection.waiting_count`
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
        * *property* :py:attr:`testme.Suite.abort`
        * *property* :py:attr:`testme.Suite.tap`
        * *method* :py:attr:`testme.Suite.__repr__`
        * *method* :py:attr:`testme.Suite.run` - run all tests
    * *class* :py:class:`testme.Test` - unit test
        * *property* :py:attr:`testme.Test.dict`
        * *property* :py:attr:`testme.Test.exception`
        * *property* :py:attr:`testme.Test.id`
        * *property* :py:attr:`testme.Test.json`
        * *property* :py:attr:`testme.Test.name`
        * *property* :py:attr:`testme.Test.passed`
        * *property* :py:attr:`testme.Test.ran`
        * *property* :py:attr:`testme.Test.reason`
        * *property* :py:attr:`testme.Test.residue`
        * *property* :py:attr:`testme.Test.result`
        * *property* :py:attr:`testme.Test.skipped`
        * *property* :py:attr:`testme.Test.tap`
        * *property* :py:attr:`testme.Test.todo`
        * *method* :py:meth:`testme.Test.run` - run this test
        * *method* :py:meth:`testme.Test.skip` - skip this test
    * *enum* :py:class:`testme.TestResult` - test result types

*******
Modules
*******

.. py:module:: testme

testme
======

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
information on failure cases).

All ``assert_`` functions accept an optional, final keyword argument 
``reason``, which is a :py:type:`str` that explains why the assertion may have 
failed. If this is omitted, a default message will be used.

In general, each type of condition :py:mod:`testme` can check for has two
assoociated assertion functions: one which affirms it, and one which negates
it.

All assertions are listed below, and are documented in full detail.

assert_contains
===============

.. version-added:: 0.1.0

.. autofunction:: assert_contains


    Assert that ``container`` contains ``instance``.

assert_does_not_contain
=======================

.. version-added:: 0.1.0

.. autofunction:: assert_does_not_contain

    Assert that ``container`` does not contain ``instance``.

assert_does_not_raise
=====================

.. version-added:: 0.1.0

.. autofunction:: assert_does_not_raise

    A context manager which asserts that no exception of type ``ex_type`` will
    be raised during its lifetime.

assert_equals
=============

.. version-added:: 0.1.0

.. autofunction:: assert_equals

   Assert that the ``left`` and ``right`` arguments are equal.

assert_false
============

.. version-added:: 0.1.0

.. autofunction:: assert_false

   Assert that the ``expression`` evaluates to ``False``.

assert_faster
=============

.. version-added:: 0.1.0

.. autofunction:: assert_faster

    A context manager which asserts that no more than ``nanos`` number of
    nanoseconds will elapse before it finishes.

assert_greater_than
===================

.. version-added:: 0.1.0

.. autofunction:: assert_greater_than

   Assert that the ``left`` argument is greater than or equal to the ``right``
   argument.

assert_greater_than_or_equal_to
===============================

.. version-added:: 0.1.0

.. autofunction:: assert_greater_than_or_equal_to

   Assert that the ``left`` argument is greater than or equal to the ``right``
   argument.

assert_inside_range
===================

.. version-added:: 0.1.0

.. autofunction:: assert_inside_range

   Assert that ``expression`` is between ``min`` and ``max`` (inclusive).

assert_instance_of
==================

.. version-added:: 0.1.0

.. autofunction:: assert_instance_of

    Assert that ``instance`` is of type ``comp_type`` or any of its subtypes.

assert_is_infinity
==================

.. version-added:: 0.1.0

.. autofunction:: assert_is_infinity

   Assert that a floating-point ``expression`` evaluates to infinity (either
   sign).

assert_is_nan
=============

.. version-added:: 0.1.0

.. autofunction:: assert_is_nan

   Assert that a floating-point ``expression`` evaluates to NaN.

assert_is_near
==============

.. version-added:: 0.1.0

.. autofunction:: assert_is_near

   Assert that an ``expression`` is within plus-or-minus ``tolerance`` of a
   ``target`` value (inclusive).

assert_is_negative
==================

.. version-added:: 0.1.0

.. autofunction:: assert_is_negative

   Assert that an ``expression`` is negative (i.e. is less than zero, 
   exclusive).

assert_is_negative_infinity
===========================

.. version-added:: 0.1.0

.. autofunction:: assert_is_negative_infinity

   Assert that a floating-point ``expression`` is negative infinity.

assert_is_none
==============

.. version-added:: 0.1.0

.. autofunction:: assert_is_none

   Assert that an ``expression`` evaluates to ``None``.

assert_is_not_nan
=================

.. version-added:: 0.1.0

.. autofunction:: assert_is_not_nan

   Assert that an ``expression`` evaluates to ``NaN``.

assert_is_not_infinity
======================

.. version-added:: 0.1.0

.. autofunction:: assert_is_not_infinity

   Assert that an ``expression`` does not evaluate to infinity (neither sign).

assert_is_not_near
==================

.. version-added:: 0.1.0

.. autofunction:: assert_is_not_near

   Assert that an ``expression`` is not within plus-or-minus ``tolerance`` of
   a ``target`` value.

assert_is_not_negative
======================

.. version-added:: 0.1.0

.. autofunction:: assert_is_not_negative

   Assert that an ``expression`` is non-negative.

assert_is_not_negative_infinity
===============================

.. version-added:: 0.1.0

.. autofunction:: assert_is_not_negative_infinity

   Assert that an ``expression`` does not evaluate not negative infinity.

assert_is_not_none
==================

.. version-added:: 0.1.0

.. autofunction:: assert_is_not_none

   Assert that an ``expression`` does not evaluate to ``None``.

assert_is_not_positive_infinity
===============================

.. version-added:: 0.1.0

.. autofunction:: assert_is_not_positive_infinity

   Assert that an ``expression`` does not evaluate to positive infinity.

assert_is_not_zero
==================

.. version-added:: 0.1.0

.. autofunction:: assert_is_not_zero

   Assert that an ``expression`` does not evaluate to zero.

assert_is_positive
==================

.. version-added:: 0.1.0

.. autofunction:: assert_is_positive

   Assert that an ``expression`` is positive.

assert_is_positive_infinity
===========================

.. version-added:: 0.1.0

.. autofunction:: assert_is_positive_infinity

   Assert that an ``expression`` evaluates to positive infinity.

assert_is_zero
==============

.. version-added:: 0.1.0

.. autofunction:: assert_is_zero

    Assert that an ``expression`` evaluates to zero.

assert_less_than
================

.. version-added:: 0.1.0

.. autofunction:: assert_less_than

   Assert that the ``left`` argument is less than the ``right`` argument.

assert_less_than_or_equal_to
============================

.. version-added:: 0.1.0

.. autofunction:: assert_less_than_or_equal_to

   Assert that the ``left`` argument is less than or equal to the ``right``
   argument.

assert_not_equals
=================

.. version-added:: 0.1.0

.. autofunction:: assert_not_equals

   Assert that the ``left`` and ``right`` arguments are not equal.

assert_not_instance_of
======================

.. version-added:: 0.1.0

.. autofunction:: assert_not_instance_of

    Assert that ``instance`` is not of type ``comp_type`` or any of its 
    subtypes.

assert_outside_range
====================

.. version-added:: 0.1.0

.. autofunction:: assert_outside_range

   Assert that ``expression`` is not between ``min`` and ``max`` (inclusive).

assert_raises
=============

.. version-added:: 0.1.0

.. autofunction:: assert_raises

    A context manager which asserts that an exception of type ``ex_type`` will
    be raised during its lifetime.

assert_slower
=============

.. version-added:: 0.1.0

.. autofunction:: assert_slower

    A context manager which asserts that no less than ``nanos`` number of
    nanoseconds will elapse before it finishes.

assert_true
===========

.. version-added:: 0.1.0

.. autofunction:: assert_true

   Assert that the ``expression`` evaluates to ``True``.

**********
Exceptions
**********

All exceptions in the :py:mod:`testme` library are direct subclasses of
:py:class:`Exception`.

Abort
=====

.. version-added:: 0.1.0

.. autoexception:: Abort

    Raised by the user to force :py:mod:`testme` to immediately abort the
    entire test suite run, regardless of how deeply nested the current test
    might be. Accepts an optional ``reason`` to explain why the test was
    aborted.

    Abort Methods
    -------------

    .. automethod:: __repr__

        The string representation of instances of this class is human-readable
        formatted and contains the ``reason`` if one was given. If 
        ``Abort.reason`` is ``None``, this will be an empty string.

AssertFail
==========

.. version-added:: 0.1.0

.. autoexception:: AssertFail

   Raised internally by all ``testme.assert_*`` functions to signal that a
   controlled test failure has occurred.

   .. warning:: 

      *Do not raise this exception directly!*  Doing so results in undefined 
      behavior. Instead, allow it to be raised for you whenever an assertion 
      function fails.
   

   AssertFail Properties
   ---------------------

   .. autoproperty:: assert_type

      Indicates the type of assertion function that raised this exception.
      Read-only.

   .. autoproperty:: reason

      Contains the ``reason`` emitted from the ``testme.assert_*`` function
      that raised this exception. Read-only.

   AssertFail Methods
   ------------------

   .. automethod:: __repr__

        The string representation of instances of this class is human-readable
        formatted and contains the :py:attr:`assert_type` and 
        :py:attr:`reason` properties.

*****
Enums
*****

Unless otherwise specified, all enum classes in :py:mod:`testme` are direct
subclasses of :py:class:`enum.StrEnum`.

AssertType
==========

.. version-added:: 0.1.0

.. autoclass:: testme.AssertType

   Lists all of the assertion functions defined in :py:mod:`testme`. Used by
   :py:class:`AssertFail` to indicate the type of assertion that caused the
   failure.

   AssertType Members
   ------------------

   .. autoattribute:: testme.AssertType.CONTAINS

   Used by the :py:func:`assert_contains` function when raising 
   :py:exc:`AssertFail` upon assertion failure.

   .. autoattribute:: testme.AssertType.DOES_NOT_CONTAIN

   Used by the :py:func:`assert_does_not_contain` function when raising
   :py:exc:`AssertFail` upon assertion failure.

   .. autoattribute:: testme.AssertType.DOES_NOT_RAISE

   Used by the :py:func:`assert_does_not_raise` function when raising
   :py:exc:`AssertFail` upon assertion failure.

   .. autoattribute:: testme.AssertType.EQUALS

   Used by the :py:func:`assert_equals` function when raising
   :py:exc:`AssertFail` upon assertion failure.

   .. autoattribute:: testme.AssertType.FALSE

   Used by the :py:func:`assert_false` function when raising
   :py:exc:`AssertFail` upon assertion failure.

   .. autoattribute:: testme.AssertType.FASTER

   Used by the :py:func:`assert_faster` function when raising
   :py:exc:`AssertFail` upon assertion failure.

   .. autoattribute:: testme.AssertType.GREATER_THAN

   Used by the :py:func:`assert_greater_than` function when raising
   :py:exc:`AssertFail` upon assertion failure.

   .. autoattribute:: testme.AssertType.GREATER_THAN_OR_EQUAL_TO

   Used by the :py:func:`assert_greater_than_or_equal_to` function when raising
   :py:exc:`AssertFail` upon assertion failure.

   .. autoattribute:: testme.AssertType.INSIDE_RANGE

   Used by the :py:func:`assert_inside_range` function when raising
   :py:exc:`AssertFail` upon assertion failure.

   .. autoattribute:: testme.AssertType.INSTANCE_OF

   Used by the :py:func:`assert_instance_of` function when raising
   :py:exc:`AssertFail` upon assertion failure.

   .. autoattribute:: testme.AssertType.IS_INFINITY

   Used by the :py:func:`assert_is_infinity` function when raising
   :py:exc:`AssertFail` upon assertion failure.

   .. autoattribute:: testme.AssertType.IS_NAN

   Used by the :py:func:`assert_is_nan` function when raising
   :py:exc:`AssertFail` upon assertion failure.

   .. autoattribute:: testme.AssertType.IS_NEAR

   Used by the :py:func:`assert_is_near` function when raising
   :py:exc:`AssertFail` upon assertion failure.

   .. autoattribute:: testme.AssertType.IS_NEGATIVE

   Used by the :py:func:`assert_is_negative` function when raising
   :py:exc:`AssertFail` upon assertion failure.

   .. autoattribute:: testme.AssertType.IS_NEGATIVE_INFINITY

   Used by the :py:func:`assert_is_negative_infinity` function when raising
   :py:exc:`AssertFail` upon assertion failure.

   .. autoattribute:: testme.AssertType.IS_NONE

   Used by the :py:func:`assert_is_none` function when raising
   :py:exc:`AssertFail` upon assertion failure.

   .. autoattribute:: testme.AssertType.IS_NOT_NAN

   Used by the :py:func:`assert_is_not_nan` function when raising
   :py:exc:`AssertFail` upon assertion failure.

   .. autoattribute:: testme.AssertType.IS_NOT_INFINITY

   Used by the :py:func:`assert_is_not_infinity` function when raising
   :py:exc:`AssertFail` upon assertion failure.

   .. autoattribute:: testme.AssertType.IS_NOT_NEAR

   Used by the :py:func:`assert_is_not_near` function when raising
   :py:exc:`AssertFail` upon assertion failure.

   .. autoattribute:: testme.AssertType.IS_NOT_NEGATIVE

   Used by the :py:func:`assert_is_not_` function when raising
   :py:exc:`AssertFail` upon assertion failure.

   .. autoattribute:: testme.AssertType.IS_NOT_NEGATIVE_INFINITY

   Used by the :py:func:`assert_is_not_negative_infinity` function when raising
   :py:exc:`AssertFail` upon assertion failure.

   .. autoattribute:: testme.AssertType.IS_NOT_NONE

   Used by the :py:func:`assert_is_not_none` function when raising
   :py:exc:`AssertFail` upon assertion failure.

   .. autoattribute:: testme.AssertType.IS_NOT_POSITIVE_INFINITY

   Used by the :py:func:`assert_is_not_positive_infinity` function when raising
   :py:exc:`AssertFail` upon assertion failure.

   .. autoattribute:: testme.AssertType.IS_NOT_ZERO

   Used by the :py:func:`assert_is_not_zero` function when raising
   :py:exc:`AssertFail` upon assertion failure.

   .. autoattribute:: testme.AssertType.IS_POSITIVE

   Used by the :py:func:`assert_is_positive` function when raising
   :py:exc:`AssertFail` upon assertion failure.

   .. autoattribute:: testme.AssertType.IS_POSITIVE_INFINITY

   Used by the :py:func:`assert_is_positive_infinity` function when raising
   :py:exc:`AssertFail` upon assertion failure.

   .. autoattribute:: testme.AssertType.IS_ZERO

   Used by the :py:func:`assert_is_zero` function when raising
   :py:exc:`AssertFail` upon assertion failure.

   .. autoattribute:: testme.AssertType.LESS_THAN

   Used by the :py:func:`assert_less_than` function when raising
   :py:exc:`AssertFail` upon assertion failure.

   .. autoattribute:: testme.AssertType.LESS_THAN_OR_EQUAL_TO

   Used by the :py:func:`assert_less_than_or_equal_to` function when raising
   :py:exc:`AssertFail` upon assertion failure.

   .. autoattribute:: testme.AssertType.NOT_EQUALS

   Used by the :py:func:`assert_not_equals` function when raising
   :py:exc:`AssertFail` upon assertion failure.

   .. autoattribute:: testme.AssertType.NOT_INSTANCE_OF

   Used by the :py:func:`assert_not_instance_of` function when raising
   :py:exc:`AssertFail` upon assertion failure.

   .. autoattribute:: testme.AssertType.OUTSIDE_RANGE

   Used by the :py:func:`assert_outside_range` function when raising
   :py:exc:`AssertFail` upon assertion failure.

   .. autoattribute:: testme.AssertType.RAISES

   Used by the :py:func:`assert_raises` function when raising
   :py:exc:`AssertFail` upon assertion failure.

   .. autoattribute:: testme.AssertType.SLOWER

   Used by the :py:func:`assert_slower` function when raising
   :py:exc:`AssertFail` upon assertion failure.

   .. autoattribute:: testme.AssertType.TRUE

   Used by the :py:func:`assert_true` function when raising
   :py:exc:`AssertFail` upon assertion failure.

TestResult
==========

.. version-added:: 0.1.0

.. autoclass:: testme.TestResult

   Lists all of the possible test result values that exist.

   TestResult Members
   ------------------

   .. autoattribute:: testme.TestResult.ABRT

      The :py:attr:`testme.Test.result` attribute will be this value if it
      was interrupted by `testme.Abort` while it is running.

   .. autoattribute:: testme.TestResult.FAIL

      The :py:attr:`testme.Test.result` attribute will be this value if the
      test function raises an exception when it is called by
      :py:meth:`testme.Test.run`.

   .. autoattribute:: testme.TestResult.PASS

      The :py:attr:`testme.Test.result` attribute will be this value if the
      test function returns without exception after calling 
      :py:meth:`testme.Test.run`.

   .. autoattribute:: testme.TestResult.SKIP

      The :py:attr:`testme.Test.result` attribute will be this value if the
      test was skipped.

   .. autoattribute:: testme.TestResult.TO_DO

      .. admonition:: Just So You Know

         This member has the underscore in the middle of its name to avoid
         confusing any user scipts grepping for the string "TODO".

      The :py:attr:`testme.Test.result` attribute will be this value if the
      test is a todo item, regardless of the outcome of
      :py:func:`testme.Test.run`.

   .. autoattribute:: testme.TestResult.WAIT

      The test is waiting to be run. All instances of `testme.Test` will have
      this result until it is run.

*******
Classes
*******

Collection
==========

.. version-added:: 0.1.0

.. autoclass:: testme.Collection

   Nested testing is implemented in :py:mod:`testme` through the ``Collection`` 
   class.

   This :py:mod:`Test` subclass is modified such that its notion of a
   test is a :py:mod:`list` of :py:class:`Test` objects, rather than a single
   :py:class:`Callable`.

   Like with the constructor for :py:class:`Test`, this constructor accepts
   mandatory numeric ``id`` and ``name`` arguments and optional ``indent``
   arguments. These arguments behave in the same manner as with their
   ancestor's counterparts. Please see :py:meth:`Test.__init__` for more
   information.

   The ``env`` argument creates a calling environment for the tests in this
   collection. Every name-to-argument mapping in this :py:type:`dict` will
   be passed into the test function of *each* :py:class:`Test` as they are
   run. If any ``call_kwargs`` are assigned to a :py:class:`Test`, they will be 
   added to the environment before passing the new environment into the
   :py:class:`Test` object's test function. Names from a :py:class:`Test`
   object's ``call_kwargs`` override those in ``env`` where collisions occur.
   See :py:meth:`Collection.run` for more information.

   This class satisfies both the *iterator* and *length* interfaces. See
   :py:meth:`Collection.__len__` and :py:meth:`Collection.__next` for more
   information.

   .. warning::

      Like with the constructor for :py:class:`Test`, the developer accepts the
      responsibility for managing unique ``id`` numbers to assign to new
      instances. This class does not track that information.

      Additionally, as of right now there is no canonical way to add a
      :py:class:`Test` or a :py:class:`Container` to another
      :py:class:`Container` outside of creating managed instances through
      methods such as :py:meth:`Container.test`, :py:meth:`Container.container`,
      etc.

      Except in specific cases where you need to load-in the state of a 
      :py:class:`Collection` manually, you should avoid using this constructor 
      directly. Instead, use the :py:meth:`Collection.collection` method to 
      create a new instance that is directly managed by the state of a parent 
      :py:class:`Collection`.

   Collection Properties
   ---------------------

   .. autoproperty:: aborted_count

      The number of :py:class:`Test` objects in this collection whose ``result``
      property is :py:attr:`TestResult.ABRT`. Read-only.

   .. autoproperty:: failed_count

      The number of :py:class:`Test` objects in this collection whose ``result``
      property is :py:attr:`TestResult.FAIL`. Read-only.

   .. autoproperty:: passed_count

      The number of :py:class:`Test` objects in this collection whose ``result``
      property is :py:attr:`TestResult.PASS`. Read-only.

   .. autoproperty:: skipped_count

      The number of :py:class:`Test` objects in this collection whose ``result``
      property is :py:attr:`TestResult.SKIP`. Read-only.

   .. autoproperty:: todo_count

      The number of :py:class:`Test` objects in this collection whose ``result``
      property is :py:attr:`TestResult.TO_DO`. Read-only.

   .. autoproperty:: waiting_count

      The number of :py:class:`Test` objects in this collection whose ``result``
      property is :py:attr:`TestResult.WAIT`. Read-only.

   Collection Methods
   ------------------

   .. automethod:: __len__

      Instances of this class have a length equal to the number of 
      :py:class:`Test` objects they store.

   .. automethod:: __next__

      Successive iterations on instances of this class yield the next
      :py:class:`Test` object being held.

   .. automethod:: __repr__

      Instances of this class have :py:type:`str` representations which consist
      of the :py:type:`str` representations of each of its :py:class:`Test`
      objects joined together with new-line separators, followed by a one-line
      human-readable summary of the entrire collection.

   .. automethod:: add_test

      Create a new :py:class:`Test` from a given ``func`` and add it to this
      collection. The name of the new :py:class:`Test` will be set to the name
      of ``func``, and it may also be given an optional ``reason``.

      The ``reason``, ``todo``, ``call_args``, and ``call_kwargs`` arguments are 
      passed as-is to the corresponding :py:class:`Test` constructor argument 
      with the same name. Please see :py:meth:`Test.__init__` for more 
      information.

   .. automethod:: collection

      Create a new, empty :py:class:`Collection` and add it to this collection.
      The new :py:class:`Collection` will be added to this collection's
      namespace under the passed-in name.

      The ``reason``, ``todo``, and ``env`` arguments are passed as-is to the
      corresponding :py:class:`Collection` constructor with the same name.
      Please see :py:meth:`Collection.__init__` for more information.
      
      The ``inherit_env`` option may be given in order to pass this instance's
      call-environment on to the new :py:class:`Collection`. This behavior
      overrides the ``env`` argument.

   .. automethod:: run

      Calls the ``run`` method of each :py:class:`Test` and 
      :py:class:`Collection` created by this instance in the order they were 
      created. If set-up and/or tear-down callback functions were assigned using 
      the :py:meth:`Collection.set_up` and :py:meth:`Collection.tear_down` 
      methods, they will be called immediately before and after each test is 
      run, respectively.

      The call-environment for each :py:class:`Test` is also prepared before 
      calling its :py:meth:`Test.run` method. This is done by combining the 
      namespace of the call-environment with the :py:class:`Test` object's 
      ``call_kwargs`` dictionary (see :py:meth:`Test.__init__` for more
      information). Names from ``call_kwargs`` will override those from the
      call-environment when collisions are found.

      If any of them
      fail (i.e. their :py:attr:`Test.result` property is 
      :py:attr:`TestResult.FAIL`), this
      instance's :py:attr:`Test.result` property will also be set to 
      :py:attr:`TestResult.FAIL`. Otherwise, it will be set to
      :py:attr:`TestResult.PASS`.

      An exception to this rule is made if this instance's 
      :py:attr:`Test.todo` property is ``True``: In that case, this instanace's 
      :py:attr:`Test.result` property will be set to :py:attr:`TestResult.TO_DO`
      regardless of the outcome of the outcome of any of the tests (success
      is still tracked and stored as the :py:attr:`Test.passed` property; it
      simply has no bearing on the results of this test collection).
      
      Returns the value that was assigned to this instance's
      :py:attr:`Collection.result` property.

      .. error ::

         You are only allowed to run a :py:class:`Test` once; so, by that token,
         you are also only allowed to run a :py:class:`Collection` once. Trying
         a second or subsequent times raises a :py:exc:`RuntimeError`.

   .. automethod:: skip

      Use decorator syntax to mark a function to be created, in the same
      manner as with :py:meth:`Collection.test`. The only difference is that
      immediately after the new 
      :py:class:`Test` is created and added to this instance, its 
      :py:meth:`Test.skip` method will be called.

      .. warning ::

         The name of this method collides with :py:meth:`Test.skip`, making
         :py:class:`Collection` and :py:class:`Suite` objects unable to be
         skipped.

   .. automethod:: set_up

      Use decorator syntax to mark a function to be used for the set-up half
      of this collection's test-fixture. 

      Immediately before each test in this collection is
      run, this function will be called with zero arguments.

      The decorated function is returned unaltered.

   .. automethod:: tear_down

      Use decorator syntax to mark a function to be used for the tear-down half
      of this collection's test-fixture.

      This function will be called immediately after each test in this
      collection returns from being run. It will be called with zero arguments.

      The decorated function is returned unaltered.

   .. automethod:: test

      Use decorator syntax to create a new :py:class:`Test` object and add it
      to this :py:class:`Collection`. The assignment of a unique 
      :py:attr:`Test.id` property is handled internally, and the
      :py:attr:`Test.name` property is assigned the same value as the name of
      the decorated function.

      All positional and keyword arguments passed into this decorator will be
      passed, as given, to the ``call_args`` and ``call_kwargs`` of the
      new :py:class:`Test` (see :py:meth:`Test.__init__` for more information).

      The decorated function is returned unaltered.

      .. tip ::

         Since this method doesn't alter the decorated function, it is
         perfectly safe to stack decorator calls with different arguments to
         very easily create parameterized tests. Just remember
         that parameterized tests created in this fashion will be processed in
         the reverse order that they appear in source (i.e. from the bottom,
         closest to the definition, and working up).

   .. automethod:: test_many

      Use decorator syntax to create multiple tests all at once and add them
      to this :py:class:`Collection`.

      One :py:class:`Test` will be created for each element in the
      ``call_tuples`` argument, which is a :py:type:`list` of ``2-tuples``
      carrying the positional-argument :py:type:`list` and the
      keyword-argument :py:type:`dict` that will be passed into the decorated
      function like ``func(*call_tuple[0], **call_tuple[1])``.

      Each new test will be given a unique :py:attr:`Test.id`, but will have
      the same :py:attr:`Test.name`: the one that is bound to the decorated 
      function.

   .. automethod:: todo

      Use decorator syntax to mark a function to be created, in the same
      manner as with :py:meth:`Collection.test`, except giving 
      ``todo=True`` when calling :py:meth:`Test.__init__`.
   
Suite
=====

.. version-added:: 0.1.0

.. autoclass:: testme.Suite

   A :py:class:`Suite` is a special subclass of :py:class:`Collection` that
   represents the root collection where all other :py:class:`Test` and
   :py:class:`Container` objects reside, either directly or indirectly.

   Its constructor accepts an optional ``name`` argument. If omitted, the name 
   of the module where this constructor is being called will be used instead.

   The ``reason``, ``env``, and ``indent`` arguments behave the same as with
   their counterpart aruments in ancestor constructors. See
   :py:meth:`Test.__init__` and :py:meth:`Collection.__init__` for more 
   information.

   .. error::

      This is a singleton class. Attempting to create more than one instance
      raises :py:exc:`TypeError`.

   Suite Properties
   ----------------

   .. autoproperty:: abort

      Indicates whether or not this :py:class:`Suite` was aborted. Read-only.

   Suite Methods
   -------------

   .. automethod:: __repr__

      An instance's :py:type:`str` representation is a human-readable summary
      of the entire test suite.

Test
====

.. version-added:: 0.1.0

.. autoclass:: testme.Test

   A :py:class:`Test` is the smallest unit of concern in the :py:mod:`testme`
   framework: a single test run.

   At a minimum, the constructor requires a numeric ``id``, a ``name``, and a 
   callback function which is the logical ``test`` itself. Optionally, a
   ``reason`` may be given which further explains this test.

   Giving the ``todo`` option marks this :py:class:`Test` as a "todo" item,
   which means this test should not be expected to pass, and that its outcome
   will not affect the results of any ancestor :py:class:`Container`.

   Pass a positional-argument :py:type:`list` to ``call_args``, or a
   keyword-argument :py:type:`dict` to ``call_kwargs`` to pass them to the
   target function when the :py:meth:`run` method is called.

   The indentation level for formatted representations of this object can be
   set with ``indent``. This behavior is format-dependent.

   .. warning::

      The developer accepts the
      responsibility for managing unique ``id`` numbers to assign to new
      instances. This class does not track that information.

      Additionally, as of right now there is no canonical way to add a
      :py:class:`Test` to a
      :py:class:`Container` outside of creating managed instances through
      methods such as :py:meth:`Container.test`, :py:meth:`Container.add_test`,
      etc.

      Except in specific cases where you need to load-in the state of a 
      :py:class:`Test` manually, you should avoid using this constructor 
      directly. Instead, use the appropriate :py:meth:`Collection` method 
      for your use case to 
      create a new instance that is directly managed by the state of a
      :py:class:`Collection` object.

   Test Properties
   ---------------

   .. autoproperty:: id

      A unique, numeric identifier for this test. Read-only.

   .. autoproperty:: name

      The name of this test. Read-only.

   .. autoproperty:: skipped

      This property will be ``True`` if :py:meth:`skip` has been called.

   .. autoproperty:: ru
