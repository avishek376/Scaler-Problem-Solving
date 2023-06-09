class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        def gcd(A, B):
            if B == 0: return A
            return gcd(B, A % B)

        prev = A[0]
        value = A[0]
        for i in range(1, len(A)):
            value = gcd(prev, A[i])
            if value == 1: return 1
            prev = value

        return value
