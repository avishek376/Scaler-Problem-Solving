The value of the B-th bit is 2^B
To find the B-th bit in A, we can directly
perform bitwise AND operation between A and 2^B.
If the bit was unset we get 0 as the result of the
biwise AND and if the bit was set then the result is
2^B
    
    TC : O(1)
    SC : O(1)