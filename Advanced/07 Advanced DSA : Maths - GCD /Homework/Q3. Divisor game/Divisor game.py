class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        def gcd(a,b):
            rem = b%a
            if rem == 0:
                return a
            return gcd(rem,a)
        lcm = B*C//gcd(B,C)
        return A//lcm
