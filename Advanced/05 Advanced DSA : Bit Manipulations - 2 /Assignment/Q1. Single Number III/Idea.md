If we use additional memory, we can directly store the count and find the integers which occur only once.
To solve without additional memory, We can use the xor operation, as the Xor of two integers gives 0.
Take the Xor of all the integers of the array. Integers that occur twice will not contribute anything to the xor value.
Suppose that the ith bit is set in the xor value, which means that exactly one of the two required numbers has that bit set.
If we then divide the array integers into two groups: one group contains all integers with the ith bit set, and the other group contains integers with 0 at the ith bit.
Each group includes one of the two required numbers, and for the rest of the numbers, both of their occurrences will be in the same group.
Now, Xor of integers in the first group gives a number that occurs exactly once. Xor of integers in the second group provides another number that appears exactly once.

    TC: O(32*N)
    SC: O(1)