The constraints are small. Have you tried doing just what the question says?
Since the constraints are small we can generate all subarrays using 2 loops. This can be done in O(N^2). Then find the sum of each subarray and if the sum is less than B we add 1 to our answer.
Note that we cannot iterate over the subarray after generating the left index and right index to find the sum as this will increase the time complexity of the solution to O(N^3). We can find the sum of each subarray in O(1) with the help of a prefix sum array, which takes an O(N) precomputation.
Please refer to the complete solution for implementation.

    TC: O(N^2)
    SC: O(1)