class Solution:
    # @param A : unsigned integer
    # @return an unsigned integer
    def reverse(self, A):
        res= 0
        for i in range(32):
            if A & 1<<i:
                res=res|(1<<(31-i))
        return res
