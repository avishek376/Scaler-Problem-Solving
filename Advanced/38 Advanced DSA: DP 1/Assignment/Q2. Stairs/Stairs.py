import sys

sys.setrecursionlimit(10 ** 8)


class Solution:
    # @param A : integer
    # @return an integer
    def climbStairs(self, A):
        res = [0 for i in range(A + 1)]

        mod = 1000000007

        def stairs(num):
            if num == 1 or num == 2:
                return num
            if res[num] != 0:
                return res[num]
            a = stairs(num - 1)
            b = stairs(num - 2)
            res[num] = (a + b) % 1000000007
            return (a + b) % 1000000007

        return stairs(A) % mod