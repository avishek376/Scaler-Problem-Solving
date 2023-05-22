import sys
sys.setrecursionlimit(10**6)
class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        if B == 0:
            return 0
        val = self.solve(A-1,B//2)
        if B % 2 == 0:
            return val
        else:
            return 1-val

