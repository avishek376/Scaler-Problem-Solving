import sys

sys.setrecursionlimit(10 ** 6)


class Solution:
    # @param A : integer
    def solve(self, A):
        def numPrint(n):
            if n == 1:
                print(1, end=" ")
                return

            numPrint(n - 1)
            print(n, end=" ")

        numPrint(A)
        print()

    '''
    
    import sys
    sys.setrecursionlimit(10**6)
    def print1toA(A):
        if(A == 0):
            return
        print1toA(A - 1)
        print(A, end = " ")
    class Solution:
        # @param A : integer
        def solve(self, A):
            print1toA(A)
            print()
            
    '''