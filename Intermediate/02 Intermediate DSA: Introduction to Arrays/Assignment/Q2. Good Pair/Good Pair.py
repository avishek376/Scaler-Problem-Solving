class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        A.sort()
        count = 0
        l = len(A)
        start = 0
        end = l - 1
        while start < end:
            if (A[start] + A[end] == B):
                count += 1
                start += start
                end -= end
            elif B > A[end] + A[start]:
                start += 1
            else:
                end -= 1
        if count > 0:
            return 1
        else:
            return 0

        '''
            approach-2
            class Solution:
            # @param A : list of integers
            # @param B : integer
            # @return an integer
            def solve(self, A, B):
                # count = 0
                for i in range(0,len(A)):
                    for j in range(i+1,len(A)):
                        if(A[i]+A[j] == B):
                            return 1
                        
                return 0


        '''
