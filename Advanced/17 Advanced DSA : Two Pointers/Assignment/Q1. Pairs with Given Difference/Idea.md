Let us formulate a two pointer approach to the this problem.
We will first sort the given array and use two pointers i and j with i = 0, j = 1.
We will have three conditions:

1. A[j] - A[i] < B --> We will increase the pointer j.
2. A[j] - A[i] > B --> We will increase the pointer i.
3. A[j] - A[-] = B --> We will increase both the pointers and add 1 to the answer.

Refer to the complete solution for more details.

    
    TC: O(N)
    SC: O(1)