class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def DecimalToAnyBase(self, A, B):
        ans = 0
        po = 1
        while A > 0:
            digit = A%B
            A //= B
            ans += digit*po
            po *= 10
        return ans