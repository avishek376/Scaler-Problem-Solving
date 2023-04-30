class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        for i in range(1, len(A)):
            A[i] += A[i - 1]
        return A