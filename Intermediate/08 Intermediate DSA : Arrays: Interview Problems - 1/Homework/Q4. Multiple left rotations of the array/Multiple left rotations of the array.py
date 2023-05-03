class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of list of integers
    def solve(self, A, B):
        ans = []
        for i in range(len(B)):
            temp = []
            ind = B[i] % len(A)
            for j in range(ind, len(A)):
                temp.append(A[j])
            for j in range(ind):
                temp.append(A[j])
            ans.append(temp);

        return ans
    '''def solve(self, A, B):
        R = []
        k = len(A)
        for i in range(len(B)):
            x = B[i] % k
            R.append(A[x:] + A[:x])

        return R'''
