class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        if (A >> B) & 1 == 1:
            A = A ^ (1 << B)
        return A