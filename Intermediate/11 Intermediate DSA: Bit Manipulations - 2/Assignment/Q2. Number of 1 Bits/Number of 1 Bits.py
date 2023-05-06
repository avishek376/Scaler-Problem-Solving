class Solution:
    # @param A : integer
    # @return an integer
    def numSetBits(self, A):

        count = 0
        while A != 0:
            if A & 1 == 1:
                count += 1
            A = A >> 1
        return count



        '''
        count = 0
        while n:
            count += 1
            n = n & (n-1)
        return count
        '''



