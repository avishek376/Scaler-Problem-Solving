Create a dynamic programming table of size n * 3. In this, dp[i][0] stores maximum of value B * A[p] for p between 1 and i. Similarly dp[i][1] stores the maximum value of B * A[p] + C * A[q] such that p <= q <= i and dp[i][2] stores maximum value of B * A[p] + C * A[q] + D * A[r] for p <= q <= r <= i.

To calculate the dp:

    dp[i][0] = max(dp[i-1][0], B * A[i])
    
    dp[i][1] = max(dp[i-1][1], dp[i][0] + C * A[i])
    
    dp[i][2] = max(dp[i-1][2], dp[i][1] + D * A[i])
    
    The answer will be stored in dp[n][2]


    TC: O(N)
    SC: O(N)