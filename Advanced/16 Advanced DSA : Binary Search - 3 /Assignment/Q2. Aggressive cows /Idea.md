We’ll do the Binary Search to find the best possible maximum difference.

Since the maximum difference ranges between 0 to max of array.
If we sort the array, the binary search starts with l = 0 and r = A[n-1],
and we’ve to find the maximum distance.

For mid in binary search, we will check whether there are B stalls such that the minimum distance is greater than equal to mid.
Finally, store the maximum value we can get.


    TC: O(NlogN)
    SC: O(1)