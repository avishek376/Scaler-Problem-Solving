class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def solve(self, A):
        n = len(A)
        m = len(A[0])
        res = [[0]*n for k in range(m)]
        for i in range(n):
            for j in range(m):
                res[j][i] = A[i][j]
        return res
