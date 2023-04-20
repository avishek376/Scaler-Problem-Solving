If the first and the last element are even and the size of the array is even, then only the answer will be “YES.”
Otherwise will be “NO,” as we can’t divide the array into subarrays that meet the given conditions in the question.

    So, if(A[0]%2 == 0 and A[n-1]%2 == 0 and n%2 == 0)
    return “YES”;

    TC: O(1)
    SC: O(1)