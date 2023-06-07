1) Observe here that if a bit is being set by an element of the array then all subarray having that element will have that bit set. Therefore when we calculate sum of all subarrays having that number, we can directly multiply number of subarrays by the value that bit is making.

2) Now, to do this an easy way will be to calculate the number of subarrays for which a bit is not set and subtract it from the total number of subarrays.

3) A[j]>>i &1 ==> if true extract ith bit and check contribution (n-index)*(1<<<i)


    TC: O(32*N)
    SC: O(1)