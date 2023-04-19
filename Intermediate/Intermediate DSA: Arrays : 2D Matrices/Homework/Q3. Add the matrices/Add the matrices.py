class Solution:
    # @param A : list of list of integers
    # @param B : list of list of integers
    # @return a list of list of integers
    def solve(self, A, B):
        # Iterating over rows
        for i in range(0, len(A)):
            # Iterating over the columns
            for j in range(0, len(A[0])):
                A[i][j] += B[i][j]
        return A