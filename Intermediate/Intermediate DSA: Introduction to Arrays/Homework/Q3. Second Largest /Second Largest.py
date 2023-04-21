class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        l = list(set(A))
        l.sort()
        if len(l) == 1:
            return -1
        return l[-2]
