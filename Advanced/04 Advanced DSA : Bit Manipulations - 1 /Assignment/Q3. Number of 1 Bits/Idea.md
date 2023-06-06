Bruteforce:
Iterate 32 times, each time determining if the ith bit is a ’1′ or not.

This solution is also machine dependent (You need to be sure that an unsigned integer is 32-bit).
In addition, this solution is not very efficient too because you need to iterate 32 times no matter what.

    TC: O(32)
    SC: O(1)

A better solution:
This special solution uses a trick which is normally used in bit manipulations.
Notice what x - 1 does to bit representation of x.
x - 1 would find the first set bit from the end, and then set it to 0, and set all the bits following it.
    
    Which means if x = 10101001010100
                                  ^
                                  |
                                  |
                                  |

                       First set bit from the end
Then x - 1 becomes 10101001010(011)

All other bits in x - 1 remain unaffected.
This means that if we do (x & (x - 1)), it would just unset the last set bit in x (which is why x&(x-1) is 0 for powers of 2).

    TC: O(No.of bits)
    SC: O(1)