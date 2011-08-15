#!/usr/bin/env node

vows = require('vows'), assert = require('assert');

var MULTIPLES = [
    3, 5, 6, 9, 10, 12, 15, 18, 20
]

vows.describe('Find the sum of the multiples of 3 or 5...').addBatch({
    'Given a Solution...' : {
        topic: function(){
            return new Solution;
        },

        'Iterating should produce the known MULTIPLES...': function(topic){
            MULTIPLES.forEach(function(n){
                assert.equal(n, topic.next());
            });
        },

        'Solving should produce the expected sums...': function(){
            assert.equal(Solution.solve_for(5), 3);

            assert.equal(Solution.solve_for(10), 23);

            assert.equal(Solution.solve_for(20), 78);
        },
    }, // END Given a solution...
}).run();


Solution = (function(){
    class = function(){
        self = this;

        self.a = 0, self.b = 0;

        self.next = function(){
            var a = self.a, b = self.b;

            if ( a <= b ) self.a += 3;

            if ( b <= a ) self.b += 5;

            return (self.a < self.b) && self.a || self.b
        };
    } // END class

    class.solve_for = function ( limit )
    {
        var i = new Solution; sum = 0;

        n = i.next();

        while ( n < limit )
        {
            sum += n; n = i.next();
        }

        return sum;
    } // END solve_for

    return class;
})(); // END Solution

var limit = 1000;

console.log('SOLUTION -- Find the sum of all the multiples of 3 or 5 below',
    limit, ':', Solution.solve_for(limit)
)

