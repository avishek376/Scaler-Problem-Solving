class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @param D : integer
    # @return an integer
    def solve(self, A, B, C, D):
        N = len(A)

        # Create a dp array to store the answers of previous states
        dp = [[float("-inf")] * 3 for _ in range(N + 1)]

        for i in range(1, N + 1):
            j = i - 1  # j is used to keep track of the previous element

            # Compute the maximum value of A[i]*B
            dp[i][0] = max(dp[j][0], A[j] * B)

            # Compute the maximum value of A[i]*B + A[j]*C
            dp[i][1] = max(dp[j][1], dp[i][0] + A[j] * C)

            # Compute the maximum value of A[i]*B + A[j]*C + A[k]*D
            dp[i][2] = max(dp[j][2], dp[i][1] + A[j] * D)

        return dp[N][2]
