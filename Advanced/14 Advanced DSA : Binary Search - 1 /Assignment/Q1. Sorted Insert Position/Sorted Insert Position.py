class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def searchInsert(self, A, B):
        n = len(A)
        s = 0
        e = n - 1
        ans = 0
        while s <= e:
            m = e-(e-s)//2
            if A[m] == B:
                return m
            elif A[m] < B:
                ans = m + 1
                s = m + 1
            elif A[m] > B:
                e = m - 1

        return ans
