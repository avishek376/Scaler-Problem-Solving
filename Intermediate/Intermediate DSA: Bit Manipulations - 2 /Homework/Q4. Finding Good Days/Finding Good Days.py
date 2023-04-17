class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        count = 0
        while A > 0:
            if A & 1 == 1:
                count += 1
            A = A >> 1
        return count
