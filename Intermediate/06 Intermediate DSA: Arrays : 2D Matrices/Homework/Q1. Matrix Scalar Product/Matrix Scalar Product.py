class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return a list of list of integers
    def solve(self, A, B):
        rows = len(A)
        cols = len(A[0])

        # res = [[0] * m for i in range(n)]

        for i in range(rows):
            for j in range(cols):
                A[i][j] = A[i][j] * B

        return A

