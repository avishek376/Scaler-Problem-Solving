class Solution:
    # @param A : list of list of integers
    # @return a list of integers
    def solve(self, A):
        rows = len(A)
        cols = len(A[0])
        lst = []
        for i in range(cols):
            summ = 0
            for j in range(rows):
                summ += A[j][i]
            lst.append(summ)
        return lst
