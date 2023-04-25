class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def power(self, A, B):
        i = 1
        res = 1
        if B == 0:
            return 1
        while i <= B:
            res = res * A
            i += 1
        return res

        '''
            class Solution:
            # @param A : integer
            # @param B : integer
            # @return an integer
            def power(self, A, B):
                # A**B will find value of B to the power of A 
                return A ** B 
                
                # O(logN)
        '''
