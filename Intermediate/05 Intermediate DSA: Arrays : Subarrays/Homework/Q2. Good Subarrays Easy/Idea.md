The constraints are small.

Since the constraints are small we can generate all subarrays using 2 loops. This can be done in O(N^2).
Then find the sum of each subarray and check both the conditions.

Note that we cannot iterate over the subarray after generating the left index and right index to find the sum as this will increase the time complexity of the solution to O(N^3). 
We can find the sum of each subarray in O(1) with the help of a prefix sum array, which takes an O(N) pre-computation.
Please refer to the complete solution for implementation.
    
    TC: O(N^2)
    SC: O(N)