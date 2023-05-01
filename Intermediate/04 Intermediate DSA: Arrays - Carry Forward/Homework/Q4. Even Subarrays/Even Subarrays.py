class Solution:
    # @param A : list of integers
    # @return a strings
    def solve(self, A):
        if len(A) % 2 == 0 and A[0] % 2 == 0 and A[-1] % 2 == 0:
            return "YES"

        return "NO"
