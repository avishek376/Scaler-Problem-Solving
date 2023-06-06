class Solution:
    # @param A : list of integers
    # @return an integer
    def findMinXor(self, A):
        # sort the array A in ascending order
        A.sort()
        # the answer will be the min of XOR of each adjacent elements
        ans = A[0] ^ A[1]
        for i in range(1, len(A)):
            ans = min(ans, A[i] ^ A[i - 1])
        return ans

'''class Solution:
    # @param A : list of integers
    # @return an integer
    def findMinXor(self, A):
        # sort the array A in ascending order
        A.sort()
        # the answer will be the min of XOR of each adjacent elements
        ans = A[0] ^ A[1]
        for i in range(1, len(A)):
            ans = min(ans , A[i] ^ A[i-1])
        return ans'''

