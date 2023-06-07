class Solution:
    # @param A : list of integers
    # @return an integer
    def cntBits(self, A):
        n = len(A)

    def checkBit(arr, j):
        if arr & (1 << j) == 0:
            return False
        else:
            return True

    res = 0
    for i in range(32):
        noOfOnes = 0
        for j in range(n):
            if checkBit(A[j], i):
                noOfOnes += 1

        res += noOfOnes * (n - noOfOnes) * 2

    return res % (10 ** 9 + 7)