class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        def isValid(A, m, B):
            cnt = 0
            for x in A:
                if x <= m:
                    cnt += 1
            return cnt >= B

        if B == 1:
            return min(A)
        l = 0
        h = max(A)
        while l <= h:
            m = l + (h - l) // 2
            if not isValid(A, m, B):
                l = m + 1
            else:
                h = m - 1
        return l
