class Solution:
    # @param A : list of list of integers
    # @return a list of integers
    def solve(self, A):
        lst = []

        n = len(A)
        m = len(A[0])
        for i in range(n):
            summ = 0
            for j in range(m):
                summ += A[i][j]
            lst.append(summ)
        return lst
