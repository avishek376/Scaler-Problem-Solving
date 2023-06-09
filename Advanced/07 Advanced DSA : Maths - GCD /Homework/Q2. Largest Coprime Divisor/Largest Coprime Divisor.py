class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def cpFact(self, A, B):
        def gcd(a, b):
            rem = b % a
            if rem == 0:
                return a
            return gcd(rem, a)

        while gcd(A, B) != 1:
            A = A // gcd(A, B)
        return A
