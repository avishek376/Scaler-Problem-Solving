class Solution:
    # @param A : list of list of integers
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B):
        n = len(A)
        m = len(A[0])
        for i in range(n):
            for j in range(m):
                if B[i][j] != A[i][j]:
                    return 0
        return 1
