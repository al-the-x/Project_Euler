import unittest2

class Test(unittest2.TestCase):
    def test_multiples_of_three_or_five ( self ):
        self.assertEqual([ 3 ],
            Solution.multiples_of_three_or_five(5))

        self.assertEqual([ 3, 5, 6, 9 ],
            Solution.multiples_of_three_or_five(10))

        self.assertEqual([ 3, 5, 6, 9, 10, 12, 15, 18 ],
            Solution.multiples_of_three_or_five(20))


    def test_solve_for ( self ):
        self.assertEquals(3, Solution.solve_for(5))

        self.assertEquals(23, Solution.solve_for(10))

        self.assertEquals(78, Solution.solve_for(20))


class Solution(object):
    @classmethod
    def multiples_of_three_or_five ( cls, from_n ):
        return [ n for n in range(1, from_n) if 0 in (n % 3, n % 5) ]

    @classmethod
    def solve_for ( cls, from_n ):
        return sum(cls.multiples_of_three_or_five(from_n))


print 'SOLUTION -- Find the sum of all the multiples of 3 or 5 below 1000: %d\n\n' % (
    Solution.solve_for(1000)
)


if __name__ == '__main__':
    unittest2.main()
