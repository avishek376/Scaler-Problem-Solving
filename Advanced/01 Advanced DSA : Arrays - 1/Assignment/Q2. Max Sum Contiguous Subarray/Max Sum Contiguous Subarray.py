class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        currSum = 0
        maxSum = -10 ** 8

        for i in range(len(A)):

            if currSum >= 0:
                currSum += A[i]
            else:
                currSum = A[i]
            maxSum = max(maxSum, currSum)
        return maxSum
