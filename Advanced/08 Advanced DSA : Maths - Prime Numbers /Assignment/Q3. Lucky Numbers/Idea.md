Firstly, create an array, let’s say isprime where isprime[i] denotes true or false if number i is prime or not.

Now, for every number in the range [1, A], calculate the number of prime divisors, and if the count of distinct prime factors for a number is 2, increment the answer.

This can be easily done in O(N * sqrt(N)).

The solution can further be optimised to run in O(N * log(N)). The idea is to use a sieve and in place of marking a number of non-prime
in the array, while using sieve, just add 1 to it for each prime you iterate. In the end, you will have the number of prime factors of each
number. Then the rest is a cakewalk. There are other kinds of sieves as well that you should check out. These are quite fast in
terms of processing.


    TC: O(NlogN)
    SC: O(N)