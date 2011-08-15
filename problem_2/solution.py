#!/usr/bin/env python2.7

import unittest

FIBONACCI = [ 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610 ]

class SolutionTest(unittest.TestCase):
    def setUp ( self ):
        self.fixture = Solution()


    def test_next_fibonacci ( self ):
        for n in FIBONACCI: self.assertEquals(n, self.fixture.next())


    def test_solve_for ( self ):
        self.assertEquals(2, Solution.solve_for(4))

        self.assertEquals(2 + 8, Solution.solve_for(8))

        self.assertEquals(2 + 8, Solution.solve_for(16))

        self.assertEquals(2 + 8 + 34, Solution.solve_for(64))

        self.assertEquals(2 + 8 + 34 + 144, Solution.solve_for(256))


class Solution(object):
    def __init__ ( self ):
        self.a = 0; self.b = 1


    def next ( self ):
        c = self.a; self.a = self.b; self.b = c + self.a

        return self.b


    @classmethod
    def solve_for ( cls, limit ):
        i = cls(); sum = 0

        n = i.next()

        while ( n <= limit ):
            if ( n % 2 == 0 ): sum += n

            n = i.next()

        return sum


if __name__ == '__main__':
    print ('SOLUTION -- By considering the terms in the Fibonacci sequence whose '
        'values do not exceed four million, find the sum of the even-valued terms: '
        "%s\n\n") % Solution.solve_for(4000000)

    unittest.main()

