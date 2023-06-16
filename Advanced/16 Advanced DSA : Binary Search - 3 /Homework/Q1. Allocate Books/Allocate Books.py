class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def books(self, A, B):
        def checkcountPage(arr, m):
            c = 1
            allotedPages = 0
            for i in range(len(arr)):
                allotedPages += arr[i]

                if allotedPages > mid:
                    c += 1
                    allotedPages = arr[i]
            return c

        l = max(A)
        h = sum(A)
        ans = -1
        if B > len(A):
            return ans
        while l <= h:
            mid = l + (h - l) // 2
            if checkcountPage(A, mid) <= B:
                ans = mid

                h = mid - 1
            else:
                l = mid + 1
        return ans
