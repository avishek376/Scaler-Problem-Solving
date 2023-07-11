class Solution:
    # @param A : list of list of integers
    # @return an integer
    def adjacent(self, A):
        # rows = len(A)
        cols = len(A[0])
    
        dp = [-1 for i in range(cols)]
        dp[0] = max(A[0][0], A[1][0])

        if cols == 1:
            return dp[0]

        dp[1] = max(max(A[0][1], A[1][1]), dp[0])

        for i in range(2, cols):
            dp[i] = max(dp[i - 1], max(A[0][i], A[1][i]) + dp[i - 2])

        return dp[cols - 1]

