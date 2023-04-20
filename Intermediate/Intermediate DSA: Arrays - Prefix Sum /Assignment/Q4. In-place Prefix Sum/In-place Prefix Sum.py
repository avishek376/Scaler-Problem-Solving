class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        summ = 0
        pf = []
        for i in range(len(A)):
            summ += A[i]
            pf.append(summ)
        return pf
