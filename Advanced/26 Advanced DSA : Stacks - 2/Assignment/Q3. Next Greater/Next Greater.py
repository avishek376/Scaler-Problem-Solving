class Solution:
    # @param A : list of integers
    # @return a list of integers
    def nextGreater(self, A):
        stck = []
        ans = [-1 for i in range(len(A))]

        for i in range(len(A)):
            while len(stck) > 0 and A[stck[-1]] < A[i]:
                ans[stck.pop()] = A[i]

            stck.append(i)
        return ans