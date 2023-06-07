class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def divide(self, A, B):
        ans = 0

        INT_MAX = 2 ** 31 - 1
        INT_MIN = -2 ** 31
        if A == 0:
            return 0
        if B == 0:
            return INT_MAX
        sign = 1
        if (A < 0 and B > 0) or (A > 0 and B < 0):
            sign = -1
        A = abs(A)
        B = abs(B)
        for i in range(31, -1, -1):

            x = B << i
            if x > A:
                continue
            else:
                A -= x
                ans += 1 << i
        ans = ans * sign

        if ans > INT_MAX or ans < INT_MIN:
            return INT_MAX
        return ans
