class Solution:
    # @param A : tuple of list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        res = 0
        for i in range(n):
            res += A[i][n-1-i]
        return res
