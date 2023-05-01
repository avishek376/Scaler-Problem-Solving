class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        i = 0

        while 2**i <= A:
            if 2**i == A:
                return 1
            elif 2**i < A:
                expI = i
            i += 1
        return (A - 2**expI ) * 2 + 1