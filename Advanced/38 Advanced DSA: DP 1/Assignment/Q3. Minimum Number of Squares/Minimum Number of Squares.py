import sys , math
sys.setrecursionlimit(10**6)
class Solution:
	# @param A : integer
	# @return an integer
	def helper(self, A, dp):
        if dp[A] != -1: return dp[A]

        ans = A
        i = 1
        while i * i <= A:
            ans = min(ans, 1 + self.helper(A - i * i, dp))
            i += 1

        dp[A] = ans
        return ans

    def countMinSquares(self, A):
        dp = [-1] * (A + 1)
        dp[0], dp[1] = 0, 1
        return self.helper(A, dp)