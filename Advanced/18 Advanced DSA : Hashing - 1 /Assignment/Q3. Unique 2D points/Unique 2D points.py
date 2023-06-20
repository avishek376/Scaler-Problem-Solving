class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        set_ = set()
        n = len(A)
        for i in range(n):
            set_.add((A[i][0], A[i][1]))

        return len(set_)
