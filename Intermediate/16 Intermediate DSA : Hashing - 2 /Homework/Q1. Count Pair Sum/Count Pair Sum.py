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
            b = B-A[i]
            if b in myDict:
                count += myDict[b]
            if A[i] in myDict:
                myDict[A[i]] += 1
            else:
                myDict[A[i]] = 1
        return count % d