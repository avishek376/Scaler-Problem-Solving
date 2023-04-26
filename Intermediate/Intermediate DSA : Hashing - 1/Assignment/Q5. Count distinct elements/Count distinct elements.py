class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        s = set()
        for i in range(n):
            s.add(A[i])
        return len(s)

