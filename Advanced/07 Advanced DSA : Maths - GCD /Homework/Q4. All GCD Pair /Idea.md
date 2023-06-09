1)Sort the array in decreasing order.

2)Highest element will always be one of the original numbers. Keep that number and remove it from the array.

3)Compute GCD of the element taken in the previous step with the current element starting from the greatest and discard the GCD value from the given array.

    TC: O(NlogN + log(max of ele.))
    SC: O(N)
