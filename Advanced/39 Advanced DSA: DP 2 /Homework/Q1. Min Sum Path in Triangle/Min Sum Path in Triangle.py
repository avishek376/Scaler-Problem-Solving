class Solution:
    # @param A : list of list of integers
    # @return an integer
    def minimumTotal(self, A):
        rows = len(A)
        cols = len(A[-1])
        dpArr = [[0] * cols for i in range(rows)]

        def minPath(arr, dpArr, i, j, r, c):
            if i == r or j == c:
                dpArr[i][j] = arr[i][j]
                return arr[i][j]

            if dpArr[i][j] != 0:
                return dpArr[i][j]

            a = minPath(arr, dpArr, i + 1, j, r, c)
            b = minPath(arr, dpArr, i + 1, j + 1, r, c)

            dpArr[i][j] = min(a, b) + arr[i][j]

            return min(a, b) + arr[i][j]

        minPath(A, dpArr, 0, 0, rows - 1, cols - 1)
        return dpArr[0][0]
