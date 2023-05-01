class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def solve(self, A):
        rows = len(A)
        cols = len(A[0])
        res = [[0] * cols for i in range(rows)]

        arr1 = [-1 for i in range(cols)]
        arr2 = [-1 for i in range(cols)]

        for i in range(rows):
            for j in range(cols):
                if A[i][j] == 0:
                    arr1[i] = 0
                    arr2[j] = 0
                else:
                    res[i][j] = A[i][j]
        for i in range(rows):
            for j in range(cols):
                if arr1[i] == 0 or arr2[j] == 0:
                    res[i][j] = 0

        return res


