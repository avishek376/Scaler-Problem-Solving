class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        summ = 0
        pf = []
        myDict = {}
        for i in range(n):
            summ += A[i]
            pf.append(summ)

        count = 0

        for i in range(n):
            if pf[i] == 0:
                count += 1
            if pf[i] in myDict:
                count += myDict[pf[i]]
                myDict[pf[i]] += 1
            else:
                myDict[pf[i]] = 1
        return count % 1000000007
