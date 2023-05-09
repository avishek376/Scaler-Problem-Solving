class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        # sort the array
        A.sort()
        n = len(A)
        # Take the minimum difference of A[1]-A[0] so that we can get the common difference
        diff = A[1]-A[0]
        for i in range(n-1):
            # Check if the the sort array common difference is not equal
            if A[i+1]-A[i] != diff:
                return 0
        return 1
