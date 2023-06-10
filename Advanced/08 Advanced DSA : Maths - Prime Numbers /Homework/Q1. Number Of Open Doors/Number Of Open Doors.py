import math
class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        # find the square root of A
        x = math.sqrt(A)
        return int(x)

'''class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        s = 1
        e = A // 2
        ans = float('inf')
        if A == 0:
            return 0
        elif A == 1:
            return 1
        while s <= e:

            mid = e + (s - e) // 2

            if mid * mid == A:
                return mid
            elif mid * mid < A:
                ans = mid
                s = mid + 1
            else:
                e = mid - 1

        return ans
'''