The idea is to iterate through the array, and for every element A[i],
calculate sum of elements from 0 to i (this can simply be done as sum += arr[i]).

If the current sum has been seen before, then there is a zero-sum array.

Hashing is used to store the sum values so that we can quickly store sum and
find out whether the current sum is seen before or not.

Calculate pfSum and
checking subarray of sum equals to 0 present or not.

    TC: O(N)
    SC: O(N)