class Solution:
    # @param A : string
    # @return a strings
    def longestPalindrome(self, A):

        def expand(l, r):
            while l >= 0 and r < len(A) and A[l] == A[r]:
                l -= 1
                r += 1

            return A[l+1 : r]

        res = ''
        for i in range(len(A)):
            # for odd length substring
            test = expand(i, i)
            if len(test) > len(res):
                res = test
            # for even length substring
            test = expand(i, i + 1)
            if len(test) > len(res):
                res = test
        return res



