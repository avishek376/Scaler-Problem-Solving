Note the net change in the number of 1s in string S when we flip bits of string S.
Say it has A 0s and B 1s. Eventually, there are B 0s and A 1s.

So, the number of 1s increased by A - B. We want to choose a subarray that maximizes this. Note that if we change 1s to -1, the sum of values will give us A - B. Then, we have to find a subarray with the maximum sum, which can be done via Kadane’s Algorithm.

    TC: O(N)
    SC: O(N)