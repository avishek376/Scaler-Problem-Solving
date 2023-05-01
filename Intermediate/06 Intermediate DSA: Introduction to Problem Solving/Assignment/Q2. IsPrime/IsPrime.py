class Solution:
    # @param A : long
    # @return an integer
    def solve(self, A):
        i = 2
        if A < 2:
            return 0
        while i*i <= A:
            if A % i == 0:
                return 0
            i += 1
        return 1