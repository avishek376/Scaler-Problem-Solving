Suppose we have array A=[A0, A1, A2… ]

Now, let’s keep iterating over this array, and if A[i] != i, We swap it with index A[i] (that’s where A[i] belongs). If
you work it out, you can always see some cycle will form.

Example:

[4, 0, 1, 3, 2]
swap_index(0,4) -> swap_index(0,2) -> swap_index(0,1) (3 swaps)
[2, 0, 1, 4, 3]
swap_index(0,2) -> swap_index(0,1) (2 swaps)
swap_index(3,4) (1 swaps)
Answers would be the sum of { individual length of cycle - 1}

Remember to use some flags to not visit the same elements again and again

    TC: O(N)
    SC: O(1)