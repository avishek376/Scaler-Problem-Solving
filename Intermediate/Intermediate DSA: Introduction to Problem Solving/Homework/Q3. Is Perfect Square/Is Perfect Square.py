class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        i = 1
        while i * i <= A:
            if i * i == A:
                return 1

            i += 1
        return 0
