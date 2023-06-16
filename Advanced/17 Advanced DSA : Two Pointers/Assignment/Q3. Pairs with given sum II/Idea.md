Let us formulate a two pointer approach to the this problem.
We will first sort the given array and use two pointers i and j with i = 0, j = Length of Array - 1.
We will have three conditions:

1. A[i] + A[j] < sum  --> We will increase the pointer i.
2. A[i] + A[j] > sum  --> We will decrease the pointer j.
3. A[i] + A[j] = sum  --> We will count the frequency of A[i] and A[j] and multiply them and add to the answer.
Note, that if A[i] and A[j] are equal in value, then we will have to change the formula instead:
freq(A[i]) * freq(A[i]) –> freq(A[i]) * (freq(A[i]) - 1) / 2
to avoid overcounting pairs.

Refer to the complete solution for more details.

TC: O(N)
SC: O(N)


**BY USING TWO POINTERS APPROACH:**

Placing i at the 0th index and j in the last. handle the duplicates as well.
TC: O(N)
SC: O(1)