class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):

        def checkOffc(arr, m):
            c = 0
            for i in range(len(arr)):
                if m == 0:
                    c += arr[i]
                else:
                    c += arr[i] // m
            return c

        l = 1
        h = min(A)
        ans = 0
        if (B > sum(A)):
            return 0
        while l <= h:
            mid = l + (h - l) // 2
            if checkOffc(A, mid) >= B:
                ans = mid
                l = mid + 1

            else:
                h = mid - 1
        return ans
