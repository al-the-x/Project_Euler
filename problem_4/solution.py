#!/usr/bin/env python2.7

import unittest

class SolutionTest(unittest.TestCase):
    def test_two_digit_solution ( self ):
        self.assertItemsEqual((9009, 99, 91), Solution.solve_for(2))


    def test_generator ( self ):
        self.assertSequenceEqual(list(xrange(99, 9, -1)), list(Solution.generator(2)))

        self.assertSequenceEqual(list(xrange(999, 99, -1)), list(Solution.generator(3)))


class Solution(object):
    @classmethod
    def generator ( cls, digits, limit = None ):
        '''
        Return a generator that describes the range of integers with "digits"
        number of places, stopping at an optional "limit" that is derived if
        omitted. This allows us to stop calculations at a known valid value.
        '''
        return ( x for x in xrange(
            int('9' * digits or 0),
            limit or int('9' * (digits - 1) or 0),
            -1 # descending
        ) )


    @classmethod
    def check ( cls, value ):
        '''
        Check that the provided integer "value" is a palindrome.  Defined for
        clarity and reuse without repetition.
        '''
        return str(value) == str(value)[::-1]


    @classmethod
    def solve_for ( cls, digits ):
        '''
        Brute force method of finding the largest palindrome, made a little
        smarter by checking for the first square that is also a palindrome and
        limiting the search to the range above that value.
        '''

        limit = next( x for x in cls.generator(digits) if cls.check(x * x) )

        values = ( (x * y, x, y)
            for x in cls.generator(digits, limit)
                for y in cls.generator(digits, x)
                    if cls.check(x * y)
        )

        return values and max(values) or limit and (limit * limit, limit, limit)


if __name__ == '__main__':
    digits = 3

    print ( 'Solution -- The largest palindrome of a %d-digit number ' % digits +
        'is %d (%d X %d)' % Solution.solve_for(digits)
    )


    unittest.main()

