class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        def fact(n):
            if n == 0:
                return 1

            return fact(n - 1) * n

        return fact(A)

