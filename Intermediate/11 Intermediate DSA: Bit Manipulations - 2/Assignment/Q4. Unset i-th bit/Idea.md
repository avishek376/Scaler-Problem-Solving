We can find if the B-th bit is set in A by performing
bitwise AND of A and 2^B. If the result is non-zero then
we subtract 2^B from A. If the bitwise AND is zero that means
the B-th bit is already unset. So, then we return A as it is.
    
    TC : O(1)
    SC : O(1)