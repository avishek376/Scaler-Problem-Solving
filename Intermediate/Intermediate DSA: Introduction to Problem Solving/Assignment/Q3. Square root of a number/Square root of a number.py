class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        i = 1
        result = 0
        while i*i <= A:
            if i*i == A:
                result = i
            else:
                result = -1
            i += 1
        return result
