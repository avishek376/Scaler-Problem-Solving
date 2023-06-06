class Solution:
    # @param A : string
    # @return a list of integers
    def flip(self, A):
        cur = 0
        maxx = 0
        l = 0
        r = 0
        ans = [-1, -1]
        # basic kadane's algorithm implementation
        for i in range(0, len(A)):
            if (A[i] == '1'):
                cur -= 1
            else:
                cur += 1

            if (cur > maxx):
                ans[0] = l + 1
                ans[1] = r + 1
                maxx = cur

            if (cur < 0):
                cur = 0
                l = i + 1
                r = i + 1
            else:
                r += 1

        if (maxx == 0):
            return []
        else:
            return ans