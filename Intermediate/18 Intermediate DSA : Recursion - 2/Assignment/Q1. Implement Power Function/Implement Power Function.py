import sys
sys.setrecursionlimit(10**6)
class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def pow(self, A, B, C):
        def mypow(a,n,m):
            if n == 0:
                return 1 % m
            elif n % 2 == 0:
                temp = mypow(a, n//2, m)
                return (temp * temp) % m
            else:
                temp = mypow(a, n-1, m)
                return (a * temp) % m

        return mypow(A,B,C)

'''import sys
sys.setrecursionlimit(10**6)
class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def pow(self, A, B, C):
        def mypow(a,n,m):
            if n == 0:
                return 1%m
            p = mypow(a,n//2,m)
            if n % 2 == 0:
                return (p*p) % m
            else:
                return ((p*p) % m * a) % m

        return mypow(A,B,C)'''

