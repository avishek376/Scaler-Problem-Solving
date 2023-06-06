class Solution:
    # @param A : integer
    # @return an integer
    def numSetBits(self, A):
        def checkBit(A,i):
            if A & (1<<i) == 0:
                return False
            return True
        count = 0
        for i in range(32):
            if checkBit(A,i):
                count += 1
        return count
