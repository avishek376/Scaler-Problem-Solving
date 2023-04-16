class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        t = 1
        n = len(A)
        summ = 0
        for i in range(n-1,-1,-1):
            summ = (summ+A[i]*t)%B
            t = (t*10)%B
        return summ
