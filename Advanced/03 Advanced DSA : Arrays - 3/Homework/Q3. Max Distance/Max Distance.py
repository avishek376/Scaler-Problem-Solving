class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maximumGap(self, A):
        res = []
        for i in range(len(A)):
            res.append([A[i],i])
        res.sort()
        minv = float('inf')
        maxv = float('-inf')
        for i in range(len(res)):
            minv = min(minv,res[i][1])
            maxv = max(maxv,res[i][1]-minv)
        return maxv
