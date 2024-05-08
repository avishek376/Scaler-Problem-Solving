class Solution:
    # @param A : integer
    # @return an integer
    def numSetBits(self, A):

        noOfSetBits = 0
        while A != 0:
            if A & 1 != 0:
                noOfSetBits += 1
            A = A >> 1
        return noOfSetBits

        '''def checkBit(A,i):
            if A & (1<<i) == 0:
                return False
            return True
        count = 0
        for i in range(32):
            if checkBit(A,i):
                count += 1
        return count'''
