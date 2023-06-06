class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        def checkBit(arr, i):
            if arr & (1 << i) == 0:
                return False
            return True

        n = len(A)
        ans = 0
        for i in range(32):
            count = 0
            for j in range(n):
                if checkBit(A[j], i):
                    count += 1
            if count % 3 == 1:
                ans = ans + (1 << i)
        return ans