class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        p = 1
        ans = 0
        while A > 0:
            rem = A % 10
            A = int(A / 10)
            ans = ans + p * rem
            p = p * B
        return ans
