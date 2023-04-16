class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        pow = 1
        for i in range(B):
            pow = (pow * A) % C
        return pow % C
