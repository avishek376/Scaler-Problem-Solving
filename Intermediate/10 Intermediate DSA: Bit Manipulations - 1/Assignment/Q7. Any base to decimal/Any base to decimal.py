class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        p = 1
        res = 0
        while A > 0:
            rem = A % 10
            A = int(A / 10)
            res = res + p * rem
            p = p * B
        return res

