import sys
sys.setrecursionlimit(10**6)
class Solution:
    # @param A : integer
    def solve(self, A):
        def num(A):
            if A == 1:
                print(1,end=" ")
                print("")
                return
            print(A,end=" ")
            num(A-1)
        return num(A)
