#!/usr/bin/env ruby

require 'test/unit'

$MULTIPLES = [ 3, 5, 6, 9, 10, 12, 15, 18, 20 ]

class SolutionTest < Test::Unit::TestCase
    def test_next_multiple
        solution = Solution.new

        $MULTIPLES.each do |n|
            assert_equal n, solution.next
        end
    end


    def test_solve_for
        assert_equal 3, Solution.solve_for(5)

        assert_equal 23, Solution.solve_for(10)

        assert_equal 78, Solution.solve_for(20)
    end
end


class Solution
    def initialize
        @a = 0; @b = 0
    end


    def next
        a, b = @a, @b

        @a += 3 if a <= b

        @b += 5 if b <= a

        @a < @b and @a or @b
    end


    def self.solve_for limit
        i = self.new; n = i.next; sum = 0

        while n < limit do
            sum += n; n = i.next
        end

        return sum
    end
end #Solution

limit = 1000

print "SOLUTION -- Find the sum of all the multiples of 3 or 5 below %d: %d\n\n" % [
    limit, Solution.solve_for(limit)
]

