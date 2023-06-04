Imagine you had the same problem but with a 1D array. 
That is if the array was sorted and find the maximum subarray.

What would be the answer? The answer will be the sum of one of the suffixes right? 
So we could check over all suffix arrays
and return the maximum sum. 

The sum of all suffix arrays can be computed in O(N).
Now apply the same logic on a 2D matrix.

What is a suffix matrix? 
     A matrix whose right lower corner is always the N*M th element. 

Now we can have iterate over all the possible top left corners which is N*M. So N*M matrices.
The sum of each of these matrices can be computed in O(1) with a precomputation of O(N*M).
Return the maximum sum of all these matrices. 

    
    TC: O(N * M)
    SC: O(N * M)