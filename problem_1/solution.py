#!/usr/bin/env python2.7

import unittest

MULTIPLES = [ 3, 5, 6, 9, 10, 12, 15, 18, 20 ]

class SolutionTest(unittest.TestCase):
    def test_next_multiple ( self ):
        solution = Solution()

        for n in MULTIPLES: self.assertEqual(n, solution.next())


    def test_solve_for ( self ):
        self.assertEquals(3, Solution.solve_for(5))

        self.assertEquals(23, Solution.solve_for(10))

        self.assertEquals(78, Solution.solve_for(20))


class Solution(object):
    def __init__ ( self ):
        self.a = 0; self.b = 0


    def next ( self ):
        a, b = self.a, self.b

        self.a += a <= b and 3

        self.b += b <= a and 5

        return self.a < self.b and self.a or self.b


    @classmethod
    def solve_for ( cls, limit ):
        i = cls(); n = i.next(); sum = 0

        while ( n < limit ):
            sum += n; n = i.next()

        return sum


if __name__ == '__main__':
    limit = 1000

    print 'SOLUTION -- Find the sum of all the multiples of 3 or 5 below %d: %d\n\n' % (
        limit, Solution.solve_for(limit)
    )

    unittest.main()
