class Solution:
    # @param A : list of list of integers
    # @return a list of integers
    def solve(self, A):
        lst = []

        rows = len(A)
        cols = len(A[0])
        for i in range(rows):
            summ = 0
            for j in range(cols):
                summ += A[i][j]
            lst.append(summ)
        return lst
