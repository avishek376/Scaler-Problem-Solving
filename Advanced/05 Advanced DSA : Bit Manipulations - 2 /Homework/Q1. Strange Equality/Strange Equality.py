class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):

        x = 0
        binLen = format(A, 'b')

        for i in range(len(binLen)):
            if A & (1 << i):
                pass
            else:
                x = x | (1 << i)

        y = 1 << len(binLen)
        return x ^ y