import sys

sys.setrecursionlimit(10 ** 6)


class Solution:
    # @param A : list of list of integers
    # @return an integer
    def minPathSum(self, A):
        rows = len(A)
        cols = len(A[0])

        dpArr = [[0] * cols for i in range(rows)]

        def dpMinPathSum(arr, dpArr, rows, cols):
            if rows < 0 or cols < 0:
                return float('inf')

            if rows == 0 and cols == 0:
                dpArr[rows][cols] = arr[rows][cols]
                return dpArr[rows][cols]

            if dpArr[rows][cols] != 0:
                return dpArr[rows][cols]

            a = dpMinPathSum(arr, dpArr, rows, cols - 1)
            b = dpMinPathSum(arr, dpArr, rows - 1, cols)

            dpArr[rows][cols] = min(a, b) + arr[rows][cols]
            return min(a, b) + arr[rows][cols]

        dpMinPathSum(A, dpArr, rows - 1, cols - 1)
        return dpArr[rows - 1][cols - 1]