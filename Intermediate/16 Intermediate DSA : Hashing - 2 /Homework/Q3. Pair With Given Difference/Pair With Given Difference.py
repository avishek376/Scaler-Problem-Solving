class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        myDict = {}

        n = len(A)
        for i in range(n):
            diff1 = A[i] + B
            diff2 = A[i] - B
            if diff1 in myDict:
                return 1
            if diff2 in myDict:
                return 1
            if A[i] in myDict:
                myDict[A[i]] += 1
            else:
                myDict[A[i]] = 1
        return 0
