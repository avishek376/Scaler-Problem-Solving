class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        result = 0
        s = set()
        for i in range(len(A)):
            if B ^ A[i] in s:
                result = result + 1
            s.add(A[i])
        return result
