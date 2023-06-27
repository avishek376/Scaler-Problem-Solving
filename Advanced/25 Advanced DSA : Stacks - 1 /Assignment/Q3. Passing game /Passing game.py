class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : list of integers
    # @return an integer
    def solve(self, A, B, C):
        stck = []
        stck.append(B)
        if len(stck) > 0:
            for i in C:
                if i != 0:
                    stck.append(i)
                else:
                    stck.pop()
        return stck[-1]
