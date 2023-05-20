class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        myDict = {}
        count = 0
        d = (10**9) + 7
        n = len(A)
        for i in range(n):
            diff1 = B+A[i]
            diff2 = A[i]-B
            if diff1 in myDict:
                count += myDict[diff1]
            if diff2 in myDict:
                count += myDict[diff2]
            if A[i] in myDict:
                myDict[A[i]] += 1
            else:
                myDict[A[i]] = 1
        return count%d
