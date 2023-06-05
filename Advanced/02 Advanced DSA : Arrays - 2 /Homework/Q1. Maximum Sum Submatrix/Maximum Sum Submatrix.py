class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        rows = len(A)
        cols = len(A[0])

        def kadanes(arr):
            summ = 0
            ans = -10 ** 8
            for i in range(len(arr)):
                if summ >= 0:
                    summ += arr[i]
                else:
                    summ = arr[i]
                ans = max(ans, summ)
            return ans

        maxi = -10 ** 8
        for k in range(cols):
            pfArr = [0 for __ in range(rows)]
            for j in range(k, cols):
                for i in range(rows):
                    pfArr[i] = (A[i][j]) + pfArr[i]
                currMax = kadanes(pfArr)
                maxi = max(maxi, currMax)

        return maxi
