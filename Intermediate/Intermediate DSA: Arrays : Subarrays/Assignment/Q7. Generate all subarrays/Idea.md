We can run two nested loops, the outer loop will consider the 
starting index for subarrays and inner loop will consider the 
ending index for subarrays. 
(For every start index(s), end index(e) varies from s to N-1)
So, by these two loops, you can iterate on all possible starting and ending index
of the subarrays, but they do not actually extract the subarrays themselves.
Hence, third inner loop is required to extract the subarray from s to e.

    TC : O(N^3)
    SC : O(N^3)