.. py:module:: testme

#############################
``testme`` - Reference Manual
#############################

This document is a complete reference manual for the ``testme`` library,
including all public API members. It is rather comprehensive, and may be
an overwhelming read for new users. To give these users an easier path to 
getting their feet wet with ``testme``, a :ref:`quick-guide` has been provided.

****************
Package Overview
****************

The following is a complete listing of the :py:mod:`testme` source tree. API
members are listed alphabetically.

* ``module`` :py:mod:`testme` - root-level module
    * ``function`` :py:func:`testme.assert_contains` - assert a container holds a 
      value
    * ``function`` :py:func:`testme.assert_does_not_contain` - assert a
      container does *not* hold a value
    * ``function`` :py:func:`testme.assert_does_not_raise` - assert a
      block of code does not raise an exception
    * ``function`` :py:func:`testme.assert_equals` - assert two values are
      equal
    * ``function`` :py:func:`testme.assert_false` - assert a value is `False`
    * ``function`` :py:func:`testme.assert_faster` - assert a block of code
      finishes faster than a duration
    * ``function`` :py:func:`testme.assert_greater_than` - assert one value
      is greater than another
    * ``function`` :py:func:`testme.assert_greater_than_or_equal_to` - assert
      one value is greater than or equal to another
    * ``function`` :py:func:`testme.assert_inside_range` - assert a value is
      between two others
    * ``function`` :py:func:`testme.assert_instance_of` - assert a value is of a
      type
    * ``function`` :py:func:`testme.assert_is_infinity` - assert a value is
      infinity
    * ``function`` :py:func:`testme.assert_is_nan` - assert a value is NaN
    * ``function`` :py:func:`testme.assert_is_near` - assert two values are near
    * ``function`` :py:func:`testme.assert_is_negative` - assert a value is
      negative
    * ``function`` :py:func:`testme.assert_is_negative_infinity` - assert a
      value is negative infinity
    * ``function`` :py:func:`testme.assert_is_none` - assert a value is ``None`` 
