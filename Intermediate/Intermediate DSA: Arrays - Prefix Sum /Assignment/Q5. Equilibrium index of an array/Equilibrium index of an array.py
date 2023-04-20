class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        summ = 0
        pf = []
        for i in range(len(A)):
            summ += A[i]
            pf.append(summ)
        count = 0

        for i in range(len(A)):
            if i == 0:
                L = 0
            else:
                L = pf[i - 1]
            if i == len(A) - 1:
                R = 0
            else:
                R = pf[len(A) - 1] - pf[i]
            if L == R:
                count += 1
                return i
        return -1


