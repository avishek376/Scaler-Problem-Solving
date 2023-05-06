class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        myDict = {}
        for i in range(n):
            if A[i] not in myDict:
                myDict[A[i]] = 1
            else:
                myDict[A[i]] += 1

        count = 0
        for i in range(n):
            if myDict[A[i]] == 1:
                count += 1
        return count
