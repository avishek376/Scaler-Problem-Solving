class Solution:
    # @param A : long
    # @param B : integer
     # @return an long
    def solve(self, A, B):
        A = A >> B           #This will loose B bits at the right
        A = A << B             #This will add B 0's at the right
        return A
