class Solution:
    # @param A : list of characters
    # @return an integer
    class Solution:
        # @param A : list of characters
        # @return an integer
        def solve(self, A):
            for x in A:
                if x >= 'a' and x <= 'z':
                    continue
                if x >= 'A' and x <= 'Z':
                    continue
                if x >= '0' and x <= '9':
                    continue
                return 0
            return 1

    '''
        def solve(self, A):
            A = ''.join(A)
            if A.isalnum():
                return 1
            else:
                return 0

        
    '''