The value of the B-th bit is 2^B
To toggle the B-th bit in A, we can directly
perform bitwise XOR operation between A and 2^B.
If the bit was set, this will unset the bit and
if the bit was unset, then this will set that 
bit
    
    TC : O(1)
    SC : O(1)