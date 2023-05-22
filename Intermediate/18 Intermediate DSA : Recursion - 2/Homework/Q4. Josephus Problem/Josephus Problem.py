import sys
sys.setrecursionlimit(10**6)
class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        def ans(A,B):
            if A == 1:
                return 1
            x = ans(A-1,B)
            y = (x+B) % A
            if y == 0:
                y = A
            return y
        return ans(A,B)
