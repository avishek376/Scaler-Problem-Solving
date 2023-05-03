class Solution:
    # @param A : list of integers
    # @return a list of integers
    class Solution:
        # @param A : list of integers
        # @return a list of integers
        def solve(self, A):
            ret = [[]]
            for i in A:
                if i < 0:
                    ret.append([])
                else:
                    ret[-1].append(i)
            mxlen = max([len(i) for i in ret])
            for i in ret:
                if len(i) == mxlen:
                    return i
    '''
    def solve(self, A):
        n = len(A)
        ans = 0
        for i in range(n):
            for j in range(i,n):
                if A[j] < 0:
                    break
                else:
                    if len(A[i:j+1]) > ans:
                        temp = A[i:j+1]
                        ans = len(A[i:j+1])
        return temp
        '''
