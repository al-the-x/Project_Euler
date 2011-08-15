#!/usr/bin/env phpunit
<?php

class SolutionTest extends PHPUnit_Framework_TestCase
{
    public $FIBONACCI = array( 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610 );

    function test_next_fibonacci ( )
    {
        $solution = new Solution;

        foreach ( $this->FIBONACCI as $n )
        {
            $this->assertEquals($n, $solution->next());
        }
    }


    function test_solve_for ( )
    {
        $this->assertEquals(2, Solution::solve_for(2));

        $this->assertEquals(2, Solution::solve_for(4));

        $this->assertEquals(2 + 8, Solution::solve_for(8));

        $this->assertEquals(2 + 8, Solution::solve_for(16));

        $this->assertEquals(2 + 8, Solution::solve_for(32));

        $this->assertEquals(2 + 8 + 34, Solution::solve_for(64));
    }
}


class Solution
{
    protected $a = 0, $b = 1;

    function next ( )
    {
        $c = $this->a; $this->a = $this->b; $this->b = $c + $this->a;

        return $this->b;
    }


    static function solve_for ( $limit )
    {
        $i = new static; $sum = 0;

        $n = $i->next();

        while ( $n <= $limit )
        {
            if ( $n % 2 == 0 ) $sum += $n;

            $n = $i->next();
        }

        return $sum;
    }
} // END Solution


echo 'SOLUTION -- By considering the terms in the Fibonacci sequence whose values ',
    'do not exceed four million, find the sum of the even-valued terms: ',
    Solution::solve_for(4000000), "\n\n";

