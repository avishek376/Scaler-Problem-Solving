class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def solve(self, A):
        n = len(A)
        m = len(A[0])
        res = [[0] * m for i in range(n)]

        arr1 = [-1 for i in range(m)]
        arr2 = [-1 for i in range(m)]

        for i in range(n):
            for j in range(m):
                if A[i][j] == 0:
                    arr1[i] = 0
                    arr2[j] = 0
                else:
                    res[i][j] = A[i][j]
        for i in range(n):
            for j in range(m):
                if arr1[i] == 0 or arr2[j] == 0:
                    res[i][j] = 0

        return res


