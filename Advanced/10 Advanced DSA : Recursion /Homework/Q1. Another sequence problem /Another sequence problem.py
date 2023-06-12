class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        if A == 0:
            return 1
        elif A == 1:
            return 1
        elif A == 2:
            return 2

        return A + self.solve(A - 1) + self.solve(A - 2) + self.solve(A - 3)
