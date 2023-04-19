class Solution:
    # @param A : list of list of integers
    # @param B : list of list of integers
    # @return a list of list of integers
    def solve(self, A, B):
        n = len(A)
        m = len(A[0])
        res = [[0]*m for i in range(n)]

        for i in range(n):
            for j in range(m):
                A[i][j] = A[i][j]-B[i][j]
        return A

