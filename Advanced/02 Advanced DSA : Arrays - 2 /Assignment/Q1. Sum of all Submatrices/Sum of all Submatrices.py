class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        res = 0
        n = len(A)
        for i in range(n):
            for j in range(n):
                cTL = (i+1) * (j+1)
                cBR = (n-i) * (n-j)
                res += cTL * cBR * A[i][j]
        return res

