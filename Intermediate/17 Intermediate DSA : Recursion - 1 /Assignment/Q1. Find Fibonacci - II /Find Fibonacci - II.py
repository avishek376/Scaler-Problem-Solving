import sys
sys.setrecursionlimit(10**6)
class Solution:
    # @param A : integer
    # @return an integer
    def findAthFibonacci(self, A):
        def fib(n):
            if n < 2:
                return n

            return fib(n-1) + fib(n-2)
        return fib(A)
