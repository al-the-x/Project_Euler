#!/usr/bin/env phpunit
<?php

require_once 'PHPUnit/Autoload.php';

class SolutionTest extends PHPUnit_Framework_TestCase
{
    function test_multiples_of_three_or_five ( )
    {
        $this->assertEquals(array( 3, ),
            Solution::multiples_of_three_or_five(5));

        $this->assertEquals(array(3, 5, 6, 9 ),
            Solution::multiples_of_three_or_five(10));

        $this->assertEquals(array(3, 5, 6, 9, 10, 12, 15, 18 ),
            Solution::multiples_of_three_or_five(20));
    }


    function test_solve_for ( )
    {
        $this->assertEquals(3, Solution::solve_for(5));

        $this->assertEquals(23, Solution::solve_for(10));

        $this->assertEquals(78, Solution::solve_for(20));
    }
}


class Solution
{
    static function multiples_of_three_or_five ( $from_n )
    {
        // NOTE: array_filter() preserves array keys, array_values() destroys them.
        return array_values(array_filter(range(1, $from_n - 1), function($n){
            return in_array(0, array($n % 3, $n % 5));
        }));
    }

    static function solve_for ( $from_n )
    {
        return array_sum(static::multiples_of_three_or_five($from_n));
    }
}

echo 'SOLUTION -- Find the sum of all the multiples of 3 or 5 below 1000: ',
    Solution::solve_for(1000), "\n\n";
