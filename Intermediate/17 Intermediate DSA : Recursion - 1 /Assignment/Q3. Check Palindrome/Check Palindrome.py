import sys

sys.setrecursionlimit(10 ** 6)


class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        s = 0
        e = len(A) - 1

        def isPalindrome(A, s, e):

            if s >= e:
                return 1
            if A[s] == A[e]:
                return isPalindrome(A, s + 1, e - 1)
            return 0

        return isPalindrome(A, s, e)


    '''
    import sys
    sys.setrecursionlimit(10**6)
    
    def checkpalindrome(A, i, j):
        if(i >= j):
            return 1
        if(A[i] == A[j]):
            return checkpalindrome(A, i+1, j-1)
        return 0
    
    class Solution:
        # @param A : string
        # @return an integer
        def solve(self, A):
            return checkpalindrome(A, 0, len(A) - 1)
    '''
