class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        summ = 0
        ans = -10 ** 8

        for i in range(len(A)):

            if summ >= 0:
                summ += A[i]
            else:
                summ = A[i]
            ans = max(ans, summ)
        return ans
