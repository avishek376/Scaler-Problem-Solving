class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def pow(self, A, B, C):

        if A == 0:
            return 0
        elif B == 0:
            return 1

        ans = self.pow(A, B // 2, C) % C
        ans = (ans * ans) % C
        if B % 2 == 1:
            ans = (ans * A) % C

        return (ans + C) % C