import sys
sys.setrecursionlimit(10**6)
class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        if B == 0:
            return 0
        # by this we can find the parent
        val = self.solve(A-1,B//2)
        #if you observe the even indexed childs are same as parent and odds are compliment
        if B % 2 == 0:
            return val
        else:
            return 1-val

