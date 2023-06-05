The smallest leftmost possible chunk is the smallest index at which A[0….i] contains all elements up to i.

We can check that if a maximum of A[0…..i] is i, then we can take it as a separate chunk.

Find the smallest possible leftmost chunk using the above idea, and after that, we can proceed similarly for the remaining part.


    TC: O(N)
    SC: O(1)