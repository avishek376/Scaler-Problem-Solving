class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        pow = 1
        ans = 0
        while (A):
            pow = pow*5
            # If last bit of n is set
            if (A & 1) == 1:
                ans += pow
            # proceed to next bit
            A = A >> 1
        return ans

2