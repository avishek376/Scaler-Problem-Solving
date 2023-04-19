class Solution:
    # @param A : list of list of integers
    # @return a list of integers
    def solve(self, A):
        n = len(A)
        m = len(A[0])
        lst = []
        for i in range(m):
            summ = 0
            for j in range(n):
                summ += A[j][i]
            lst.append(summ)
        return lst
