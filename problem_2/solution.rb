#!/usr/bin/env ruby

require 'test/unit'

$fibonacci = [ 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610 ]

class SolutionTest < Test::Unit::TestCase
    def setup
        @fixture = Solution.new
    end


    def test_fibonacci
        $fibonacci.each do |n|
            assert_equal n, @fixture.fibonacci
        end
    end


    def test_singleton
        assert_instance_of(Solution, Solution.instance)
    end


    def test_solve_for
        assert_equal 2, Solution.solve_for(4)

        assert_equal 2 + 8 + 34, Solution.solve_for(8)

        assert_equal 2 + 8 + 34 + 144 + 610, Solution.solve_for(14)
    end
end


class Solution
    def fibonacci
        c = (@a ||= 0); @a = (@b ||= 1); @b = c + @a
    end


    def self.instance reset = false
        @@instance = Solution.new if reset

        @@instance ||= Solution.new
    end


    def self.solve_for limit
        self.instance :reset => true; sum = 0

        limit.times do
            n = self.instance.fibonacci

            sum += n if ( n % 2 == 0 )
        end

        return sum
    end
end

#print 'SOLUTION -- By considering the terms in the Fibonacci sequence whose ',
#    'values do not exceed four million, find the sum of the even-valued terms: ',
#    Solution.solve_for(4000000)
