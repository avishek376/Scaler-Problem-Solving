class Solution:
    # @param A : list of characters
    # @return a list of characters
    def to_lower(self, A):

        for i in range(len(A)):
            if A[i].isupper():
                A[i] = (chr(ord(A[i]) ^ (1 << 5)))

        return A