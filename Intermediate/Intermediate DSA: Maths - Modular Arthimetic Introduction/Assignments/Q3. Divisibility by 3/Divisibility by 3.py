class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        res = 0
        for i in range(len(A)):
            res += A[i]
        if res % 3 == 0:
            return 1
        else:
            return 0
