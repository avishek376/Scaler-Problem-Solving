class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return a list of integers
    def solve(self, A, B, C):
        start = B
        end = C

        while(start<end):
            temp = A[start]
            A[start] = A[end]
            A[end] = temp
            start += 1
            end -= 1
        return A
