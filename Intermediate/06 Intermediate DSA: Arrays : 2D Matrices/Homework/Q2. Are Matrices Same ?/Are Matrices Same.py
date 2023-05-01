class Solution:
    # @param A : list of list of integers
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B):
        rows = len(A)
        cols = len(A[0])
        for i in range(rows):
            for j in range(cols):
                if B[i][j] != A[i][j]:
                    return 0
        return 1
