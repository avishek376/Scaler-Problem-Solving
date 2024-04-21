Approach using **Two Pointers**

Sort the given array, now we can apply two pointer based approach to solve this problem. Simply maintain two pointers
forward and end.Now traverse the array using these pointers, let the sum of elements under these pointers be Cur_sum.

* if Cur_sum == A , then return true.
* if Cur_sum > A , then decrease the end pointer.
* if Cur_sum < A , then increment the forward pointer.

    TC:O(NlogN) + O(N)
    SC:O(1)

***
Approach using **sets**

We can traverse the array B from left to right, inserting the elements of the array into a set. Now for an element, we
check if A - B[i] is already present in the set or not.

    TC: O(N)
    SC : O(N)

where N is the size of the array B