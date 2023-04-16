class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):

        if (A >> B) & 1 == 1:
            return 1
        else:
            return 0
