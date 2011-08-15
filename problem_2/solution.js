#!/usr/bin/env node

vows = require('vows'), assert = require('assert');

var FIBONACCI = [ 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610 ];

vows.describe('Find the sume of the even-numbered Fibonacci numbers...').addBatch({
    'Given a Solution...': {
        topic: function(){
            return new Solution;
        },

        'Iterating should produce the FIBONACCI numbers...': function(topic){
            FIBONACCI.forEach(function(n){
                assert.equal(n, topic.next());
            });
        },

        'The "solve_for" method should produce the expected sums...': function(){
            assert.equal(2, Solution.solve_for(4));

            assert.equal(2 + 8, Solution.solve_for(8));

            assert.equal(2 + 8, Solution.solve_for(16));

            assert.equal(2 + 8 + 34, Solution.solve_for(64));

            assert.equal(2 + 8 + 34 + 144, Solution.solve_for(256));
        },
    }, // END Given a Solution...
}).run();


Solution = (function(){
    class = function(){
        self = this;

        self.a = 0; self.b = 1;

        self.next = function()
        {
            c = self.a; self.a = self.b; self.b = c + self.a;

            return self.b;
        }
    } // END class

    class.solve_for = function ( limit )
    {
        i = new Solution; sum = 0;

        n = i.next();

        while ( n <= limit )
        {
            if ( n % 2 == 0 ) sum += n;

            n = i.next();
        }

        return sum;
    } // END solve_for

    return class;
})(); // END Solution


console.log('SOLUTION -- By considering the terms in the Fibonacci sequence whose',
    'values do not exceed four million, find the sum of the even-valued terms:',
    Solution.solve_for(4000000), "\n\n"
);

