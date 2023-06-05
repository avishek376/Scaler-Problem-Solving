class Solution:
    # @param A : list of integers
    # @return an integer
    def maxArr(self, A):
        n = len(A)

        if len(A) == 1:
            return 0

        X_MAX, X_MIN = float('-inf'), float('inf')
        Y_MAX, Y_MIN = float('-inf'), float('inf')
        ans = max((X_MAX - X_MIN), (Y_MAX - Y_MIN))

        for i in range(n):
            X = A[i] - i
            Y = A[i] + i
            # update X_MAX, X_MIN, Y_MAX, Y_MIN
            X_MAX, X_MIN = max(X, X_MAX), min(X, X_MIN)
            Y_MAX, Y_MIN = max(Y, Y_MAX), min(Y, Y_MIN)

        ans = max((X_MAX - X_MIN), (Y_MAX - Y_MIN))

        return ans
