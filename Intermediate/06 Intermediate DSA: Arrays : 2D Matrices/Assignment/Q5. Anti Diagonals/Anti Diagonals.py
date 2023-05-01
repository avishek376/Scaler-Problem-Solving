class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def diagonal(self, A):
        n = len(A)
        p = len(A[0])
        m = 2 * n - 1
        res = [[] for i in range(m)]

        for i in range(n):
            for j in range(p):
                res[i + j].append(A[i][j])
        for i in range(m):
            while len(res[i]) < p:
                res[i].append(0)

        return res
