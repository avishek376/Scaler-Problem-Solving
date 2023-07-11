Suppose dp[i][j] represents the number of unique paths to reach cell (i, j).

To calculate dp[i][j], consider the following:

If cell (i, j) does not have an obstacle, the number of ways to reach this cell is the sum of the number of ways to reach the immediate neighbors preceding it (left and up).

If cells (i-1, j) and (i, j-1) both do not have obstacles, then dp[i][j] = dp[i-1][j] + dp[i][j-1].

If only cell (i-1, j) does not have an obstacle, then dp[i][j] = dp[i-1][j].

If only cell (i, j-1) does not have an obstacle, then dp[i][j] = dp[i][j-1].

If both cells (i-1, j) and (i, j-1) have obstacles, set dp[i][j] = 0.

Finally, the value of dp[n][m] will be the answer.

    
    TC: O(N*M)
    SC: O(N*M)