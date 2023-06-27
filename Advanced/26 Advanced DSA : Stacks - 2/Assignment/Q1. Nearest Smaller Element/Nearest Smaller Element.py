class Solution:
	# @param A : list of integers
	# @return a list of integers
    def prevSmaller(self, A):
        ans = [-1 for i in range(len(A))]
        stck = []
        for i in range(len(A)-1,-1,-1):
            while len(stck)>0 and A[stck[-1]]>A[i]:
                ans[stck.pop()] = A[i]
            stck.append(i)
        return ans
