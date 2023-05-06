We can use the two following properties:

(a * b) mod x = [(a mod x) * (b mod x)] mod x

(a + b) mod x = [(a mod x) + (b mod x)] mod x


We can represent a number [a, b, c, d] as (a * 1000) + (b * 100) + (c * 10) + (d * 1).
We can use the above properties of modular arithmetic to solve the problem.

We will iterate from the end of the array (least significant digit).
We will keep a variable that will store the values of powers of 10 modulo B at every step.
Then, we will perform the operations accordingly.
Be careful of integer overflows.

Refer to the complete solution for more implementation details.

    TC : O(N)
    SC : (1)