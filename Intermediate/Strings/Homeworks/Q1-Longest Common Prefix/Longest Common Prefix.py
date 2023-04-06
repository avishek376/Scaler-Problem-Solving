class Solution:
    # @param A : list of strings
    # @return a strings
    def longestCommonPrefix(self, A):
        lcp = ""

    if len(A) == 0:
        return lcp
    minlen = len(A[0])
    for i in range(len(A)):
        minlen = min(len(A[i]), minlen)

    i = 0
    while (i < minlen):
        currentChar = A[0][i]
        for j in range(1, len(A)):

            if A[j][i] != currentChar:
                return lcp
        lcp += currentChar
        i += 1
    return lcp
