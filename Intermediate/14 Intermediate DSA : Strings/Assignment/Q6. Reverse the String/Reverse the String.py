class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        A = A.strip()
        A = A.split()
        j=""
        j = " ".join(A[::-1])
        return j