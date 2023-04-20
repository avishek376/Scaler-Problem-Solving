class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
    # @return an list of long
    def rangeSum(self, A, B):
        lst = []
        summ = 0
        pf = []
        for i in range(len(A)):
            summ += A[i]
            pf.append(summ)
        for j in B:
            L = j[0] - 1
            R = j[1] - 1
            if L == 0:
                lst.append(pf[R])
            else:
                lst.append(pf[R] - pf[L - 1])
        return lst




