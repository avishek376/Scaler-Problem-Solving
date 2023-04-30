class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):

        n = len(A)
        pref = [0] * n
        suff = [0] * n
        pref[0] = A[0]
        for i in range(1, n):
            pref[i] = pref[i - 1] * A[i]
        suff[n - 1] = A[n - 1]
        for i in range(n - 2, -1, -1):
            suff[i] = suff[i + 1] * A[i]
        ans = [0] * n
        for i in range(n):
            if (i == 0):
                ans[i] = suff[i + 1]
            elif i == n - 1:
                ans[i] = pref[i - 1]
            else:
                ans[i] = pref[i - 1] * suff[i + 1]
        return ans
