If any element in the array is even then, it can be made 0. Split that element into two equal parts of A[i]/2 and A[i]/2. XOR of two identical numbers is zero. Therefore this strategy makes an element 0.

If any element is odd. Split it in two-part: 1, A[i]-1. Since A[i]-1 is even, it can be made 0 by the above strategy. Therefore an odd element can reduce its size to 1.

Therefore, two odd elements can be made 0 by following the above strategy and finally XOR them (i.e., 1) as 1 XOR 1 = 0.

Therefore if the number of odd elements in the array is even, the answer is possible. Otherwise, an element of value 1 will be left, and it is impossible to satisfy the condition.

    TC: O(N)
    SC: O(1)