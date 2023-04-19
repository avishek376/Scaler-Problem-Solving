Since, the length of the given required subarray is fixed, and the constraints allow an O(N ^ 2) approach.

We can simply brute force for each subarray for length 2 * B + 1.
We will loop from each starting point of every possible subarray, and check if the adjacent elements are unequal.

We can keep a flag variable to keep track of the status throughout the subarray.
If the condition is true, then we will append to a list that we will return.

Refer to the complete solution for more implementation details.
    
    TC: O((N-B+1)*B)
    SC: O(N)