class Solution:
    # @param A : list of integers
    # @return a strings
    def solve(self, A):
        val = 0
        n = len(A)
        for i in range(n):
            val = val^A[i]

        if val%2 == 0:
            return "Yes"
        return "No"
