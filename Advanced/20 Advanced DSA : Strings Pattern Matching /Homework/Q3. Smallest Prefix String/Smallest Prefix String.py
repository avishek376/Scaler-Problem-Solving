class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def smallestPrefix(self, A, B):
        n = len(A)
        str = ""
        i = 1
        str += A[0]

        while i < n:
            if ord(A[i]) < ord(B[0]):
                str += A[i]
            else:
                break
            i += 1
        str += B[0]
        return str
