class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        if A == 1:
            return 0
        s = 1
        for j in range(2, A + 1):
            if j * j > A:
                break
            if A % j == 0:
                s += j
                if (A // j) != j:
                    s += A // j
        if s == A:
            return 1
        return 0
