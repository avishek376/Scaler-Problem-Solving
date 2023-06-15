class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        def gcd( B, C):
            if C == 0:
                return B
            return gcd(C, B % C)

        def magic_num_count( A, B, C, LCM):
            return (A // B) + (A // C) - (A // LCM)


        mod = 1000000007
        GCD = gcd(B, C)
        LCM = (B * C) // GCD

        # binary search
        low = 1

        # the largest value for which we can find the smallest Ath
        # magical number is the Ath multiple of the smaller
        # of B or C.
        high = min(B, C) * A
        floor = 0
        while low <= high:
            mid = (low + high) // 2
            magic = magic_num_count(mid, B, C, LCM)
            if magic >= A:
                floor = mid
                high = mid - 1
            else:
                low = mid + 1

        return floor % mod
