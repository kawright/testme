# basic_ex.py - a basic example of the testme framework

# testme - unit testing framework
#
# Copyright (C) 2026  Kristoffer A. Wright
# See 'LICENSE' for details

import sys
from pathlib import Path

sys.path.insert(0, str(Path('.', 'src').resolve()))

#####

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
