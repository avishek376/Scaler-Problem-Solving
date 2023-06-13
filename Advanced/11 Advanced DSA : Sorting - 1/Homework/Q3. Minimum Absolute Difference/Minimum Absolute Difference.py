class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        A.sort()
        min1 = 10 ** 8
        diff = 0

        for i in range(n - 1):
            diff = A[1 + i] - A[i]
            min1 = min(min1, diff)

        return min1

'''
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        # sort the array 
        A.sort()
        # initialize the ans variable
        ans = A[1] - A[0]
        for i in range(1, n):
            # store the minimum value
            ans = min(ans, A[i] - A[i - 1])
        return ans
'''