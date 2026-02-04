.. _quick-guide:

###################
testme  Quick Guide
###################

:py:mod:`testme` is a test framework that strives to minimize the syntax needed to
write complete tests while maintaining a robust set of features. 
:py:mod:`testme` includes:

* Friendly API that models tests as objects-to-be-handled, rather than 
  as classes-to-be-extended.
* Effortless parameterized testing.
* Nested testing through test collections.
* Test-fixtures through set-up and tear-down functions, as well as environment
  variables.
* Ability to skip tests, mark them as todo items, or abort entire test suites
  on-the-fly.
* Rich test metadata, including test names, reasons, result status, and
  additional "residue" output.
* Friendly human-readable text output.
* Out-of-the-box support for the Test Anything Protocol (TAP) version 14 format.

*************
Basic Example
*************

Here's a small demonstration to show you how easy it is to test your code with
:py:mod:`testme`::

    # basic_example.py

    import testme

    def add_two_numbers(left, right):
        return left + right

    suite = testme.Suite()

    @suite.test(0, 0)
    @suite.test(12, 5)
    @suite.test(-9, 9) 
    def test_add_two_numbers(left, right):
        expected = left + right
        real = add_two_numbers(left, right)
        testme.assert_equals(real, expected)
        return real

    def main():
        suite.run()
        print(suite)
        exit(0)

    if __name__ == "__main__":
        main()

Which produces the following output::

    $ python3 ./basic_example.py

    0. PASS [x]: basic_example()
        1. PASS [x]: test_add_two_numbers(-9, 9) -> 0
        2. PASS [x]: test_add_two_numbers(12, 5) -> 17
        3. PASS [x]: test_add_two_numbers(0, 0) -> 0
    <<3 passed, 0 failed, 0 waiting, 0 skipped, 0 todo, 0 aborted, 3 TOTAL>>

This is just a small subset of the features included with ``testme``. The rest
of this manual covers all of these features in further detail.

************************************************
Building Blocks - The `Test` and `Suite` Classes
************************************************

At its core, the concept of software testing rests on two building blocks: the 
individual test, and a collection of tests, which we call a test-suite. In
:py:mod:`testme`, these concepts are modeled with the :py:class:`Test` and 
:py:class:`Suite` classes.

Let's start by taking a quick glance at each of these classes, starting with
the :py:class:`Suite` class:

.. autoclass:: Suite

    Create a new :py:class:`Suite` with an optional ``name`` and ``reason``.

    The :py:Class:`Suite` class represents an entire test-suite in the
    :py:mod:`testme` library. It contains numerous instances of :py:class:`Test` 
    and :py:Class:`Collection` which are executed when the test-suite is run.

    The :py:mod:`Suite` class, just like the :py:mod:`Collection` class, is
    a sub-class of the :py:mod:`Test` class. Methods, attributes, and
    properties of the :py:mod:`Collection` and :py:mod:`Test` classes which are
    not documented here are assumed to be inherited. Those which *are* are
    assumed to be overridden.

    This is a singleton class. Attempting to create more than one will raise
    :py:exc:`TypeError`.

    If no ``name`` is given, the name of the current module is used.

    If the ``todo`` option is given, this entire suite will be considered a
    "TODO" item, meaning that the outcome of the tests it contains will not
    affect the result of the entire :py:class:`Suite` run: it will be
    :py:attr:`TestResult.TODO` no matter what.

    The ``env`` and ``ident`` arguments behave in the same manner as with the
    constructor for the :py:class:`Collection` class.

The 
