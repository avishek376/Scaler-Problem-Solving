class Solution:
    # @param A : list of integers
    # @return a list of integers
    def subUnsort(self, A):
        ans = []
        n = len(A)
        i, j = 0, n - 1
        while (i < n - 1 and A[i] <= A[i + 1]):
            i += 1
        while (j > 0 and A[j] >= A[j - 1]):
            j -= 1

        if (i == n - 1):
            # if array is already sorted, output -1
            ans = [-1]
            return ans

        # find the maximum and and minimum element from A[i]...A[j]
        mn, mx = A[i + 1], A[i + 1]
        for k in range(i, j + 1):
            mx = max(mx, A[k])
            mn = min(mn, A[k])

        l, r = 0, n - 1
        while (A[l] <= mn and l <= i):
            l += 1
        while (A[r] >= mx and r >= j):
            r -= 1

        ans = [l, r]
        return ans