Approach 1

For every i run a loop of j and check if A[i]+A[j]==B or not. Also, check if i!=j.

Time complexity : O(n^2)

This is enough to pass the test casses. However we can furthur optimize this solution.

Approach 2

Sort the array A in increasing order. For each i from 0 to n-1 find the first element in the array having a value greater than or equal to B-A[i] using binary search.
(For c++ we can directly use ‘lower_bound’ function) . Now just check if this element is equal to B-A[i] , if it is then return 1 , otherwise continue the process.

    TC : O(nlogn)
    SC: O(1)