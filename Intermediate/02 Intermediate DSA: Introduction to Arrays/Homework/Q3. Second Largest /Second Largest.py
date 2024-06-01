'''
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        l = list(set(A))
        l.sort()
        if len(l) == 1:
            return -1
        return l[-2]

TC: O(NlogN)
SC: O(1)
'''

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        if len(A) == 1:
            return -1
        maxEle = -1
        for i in A:
            if maxEle < i:
                maxEle = i

        secondMax = -1
        for i in range(len(A)):
            if A[i] == maxEle:
                continue
            elif secondMax < A[i]:
                secondMax = A[i]

        return secondMax

# TC: O(N)
# SC: O(1)