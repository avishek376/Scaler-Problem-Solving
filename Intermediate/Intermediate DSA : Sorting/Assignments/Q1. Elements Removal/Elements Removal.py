class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        A.sort(reverse=True)
        c = 0
        for i in range(n):
            c += A[i] * (i + 1)

        return c

