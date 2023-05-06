class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        n = len(A)
        s = ""
        if n <= 3:
            s = A
        else:
            s = A[n-3] + A[n-2] + A[n-1]
        num = int(s)
        if num%8 == 0:
            return 1
        return 0