class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        def num(n):
            if n == 0:
                return n
            return n % 10 + num(n // 10)

        return num(A)
