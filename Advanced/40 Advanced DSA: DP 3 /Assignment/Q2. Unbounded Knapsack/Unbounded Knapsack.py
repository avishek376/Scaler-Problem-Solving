import sys

sys.setrecursionlimit(10 ** 6)


class Solution:
    # @param A : integer
    # @param B : list of integers
    # @param C : list of integers
    # @return an integer
    def solve(self, A, B, C):
        n = len(B)
        dp = [[-1] * (A + 1) for i in range(n)]

        def helper(i, w, v, k):
            if i < 0 or k == 0:
                return 0
            if dp[i][k] != -1:
                return dp[i][k]

            b = -1
            a = helper(i - 1, w, v, k)
            if w[i] <= k:
                b = helper(i, w, v, k - w[i]) + v[i]

            dp[i][k] = max(a, b)
            return max(a, b)

        return helper(n - 1, C, B, A)



'''

class Solution:
    # @param A : integer
    # @param B : list of integers
    # @param C : list of integers
    # @return an integer
    def solve(self, A, B, C):
        W = A
        dp = [0 for i in range(W + 1)]
        n = len(B)
        ans = 0

        # Fill dp[] using above recursive formula
        for i in range(W + 1):
            for j in range(n):
                if C[j] <= i:
                    dp[i] = max(dp[i], dp[i - C[j]] + B[j])

        return dp[W]
        
'''