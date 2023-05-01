class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProfit(self, A):
        n = len(A)

        if n == 0:
            return 0
        # here we are selling at same day
        greatest_till = 0
        profit = 0
        for i in range(n - 1, -1, -1):
            greatest_till = max(A[i], greatest_till)
            diff = greatest_till - A[i]
            profit = max(profit, diff)

        return profit

