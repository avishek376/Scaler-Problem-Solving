class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        temp = (A%100)
        if A % 400 == 0:
            return 1
        elif A % 100 == 0:
            return 0
        elif temp % 4 == 0:
            return 1
        return 0
