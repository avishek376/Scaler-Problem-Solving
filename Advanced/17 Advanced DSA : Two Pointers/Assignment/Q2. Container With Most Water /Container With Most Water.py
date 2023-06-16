class Solution:
    # @param A : list of integers
    # @return an integer
    def maxArea(self, A):
        n = len(A)

        i = 0
        j = n - 1
        ans = float('-inf')
        if n == 1:
            return 0
        while i < j:
            waterCap = (j - i) * min(A[j], A[i])
            ans = max(ans, waterCap)

            if A[i] < A[j]:
                i += 1

            else:
                j -= 1
        return ans
