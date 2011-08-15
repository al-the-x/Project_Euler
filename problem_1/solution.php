#!/usr/bin/env phpunit
<?php

class SolutionTest extends PHPUnit_Framework_TestCase
{
    protected $MULTIPLES = array( 3, 5, 6, 9, 10, 12, 15, 18, 20 );

    function test_next_multiple ( )
    {
        $solution = new Solution;

        foreach ( $this->MULTIPLES as $n ) $this->assertEquals($n, $solution->next());
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
    protected $a = 0, $b = 0;


    function next ( )
    {
        $a = $this->a; $b = $this->b;

        $this->a += ( $a <= $b ? 3 : 0 );

        $this->b += ( $b <= $a ? 5 : 0 );

        return ( $this->a < $this->b ? $this->a : $this->b );
    }


    static function solve_for ( $limit )
    {
        $i = new static; $n = $i->next(); $sum = 0;

        while ( $n < $limit )
        {
            $sum += $n; $n = $i->next();
        }

        return $sum;
    }
} // END Solution


echo 'SOLUTION -- Find the sum of all the multiples of 3 or 5 below 1000: ',
    Solution::solve_for(1000), "\n\n";

