Since the sizes of the two strings may be different, we first make the size of the smaller string equal to that of the bigger one by adding leading 0s for simplicity. Note that you can handle the addition without adding zeroes by adding a few if statements. After making sizes the same, we add bits from the rightmost bit to the leftmost bit.
In every iteration, we must sum 3 bits: 2 bits of 2 given strings and carry.
The sum bit will be 1 if all 3 bits are set, or one of them is set.

So we can add all the bits and then take the remainder with 2 to get the current bit in the answer. How to find the carryover? Carry will be 1 if any of the two bits is set. So we can find carry by adding the bits and dividing the result by 2. Following is a step-by-step algorithm: 1. Make them equal-sized by adding 0s at the beginning of the smaller string. 2. Perform bit addition Boolean expression for adding 3 bits a, b, c Sum = (a + b + c) % 2 Carry = (a + b + c ) / 2

    let length og 1st String is N & 2nd is M
    TC: O(max(N,M)+1)
    SC: O(1)