#!/usr/bin/env ruby

require 'test/unit'

$fibonacci = [ 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610 ]

class SolutionTest < Test::Unit::TestCase
    def test_next_fibonacci
        solution = Solution.new

        $fibonacci.each do |n|
            assert_equal n, solution.next
        end
    end


    def test_solve_for
        assert_equal 2, Solution.solve_for(4)

        assert_equal 2 + 8, Solution.solve_for(8)

        assert_equal 2 + 8, Solution.solve_for(16)

        assert_equal 2 + 8 + 34, Solution.solve_for(64)

        assert_equal 2 + 8 + 34 + 144, Solution.solve_for(256)
    end
end


class Solution
    def next
        c = (@a ||= 0); @a = (@b ||= 1); @b = c + @a
    end


    def self.solve_for limit
        i = self.new; sum = 0

        n = i.next

        while n <= limit do
            sum += n if ( n % 2 == 0 )

            n = i.next
        end

        return sum
    end
end

print 'SOLUTION -- By considering the terms in the Fibonacci sequence whose ',
    'values do not exceed four million, find the sum of the even-valued terms: ',
    "%s\n\n" % Solution.solve_for(4000000)
