class Solution:
    # @param A : list of list of integers
    # @param B : list of list of integers
    # @return a list of list of integers
    def solve(self, A, B):
        rows = len(A)
        cols = len(A[0])
        res = [[0]*cols for i in range(rows)]

        for i in range(rows):
            for j in range(cols):
                A[i][j] = A[i][j]-B[i][j]
        return A

