class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        myDict = {}
        lst = []
        for i in range(n):
            if A[i] not in myDict:
                myDict[A[i]] = 1
            else:
                myDict[A[i]] += 1

        for i in range(n):
            if myDict[A[i]] <= 1:
                pass
            else:
                return A[i]
        return -1