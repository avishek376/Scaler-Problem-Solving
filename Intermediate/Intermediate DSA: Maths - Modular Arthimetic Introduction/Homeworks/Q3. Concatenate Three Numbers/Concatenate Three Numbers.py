class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        ''' approach: 2'''
        start = min(A,B,C)
        end = max(A,B,C)
        mid = A+B+C - start - end
        return str(start) + str(mid)+ str(end)

        '''
        approach 1
        
        class Solution:
        
            def solve(self, A, B, C):
            
                return int(''.join([str(x) for x in sorted([A, B, C])]))
                
        '''