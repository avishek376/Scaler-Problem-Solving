class Solution:
    # @param A : integer
    # @param B : list of integers
     # @return an long
    def solve(self, A, B):
        ans, res = 0, 0
        for i in range(A):
            if B[i] == 1:
                res = i + 1
            ans += res
        return ans
