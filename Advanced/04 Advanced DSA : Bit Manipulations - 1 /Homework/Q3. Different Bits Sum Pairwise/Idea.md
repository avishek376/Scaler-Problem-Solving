Assume that all values in input have only 1 bit i.e. Ai = 0 or 1.
Lets say A = count of elements which are 0
and B = count of elements which are 1

In this case, our answer is just 2 * A * B since each such pair contributes 1 to the answer.

Can you combine this logic if we have multiple bits?

Note that all bits are independent in counting since we count the number of bits that are different in each pair.
So, we do the same process for all different bits. Since Ai is an integer, we have to do this for all 31 different bits, so our solution is O(31*N).

    TC: O(32*N)
    SC: O(1)