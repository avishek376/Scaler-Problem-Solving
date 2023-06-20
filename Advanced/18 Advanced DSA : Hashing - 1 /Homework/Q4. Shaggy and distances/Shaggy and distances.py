class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        mydict = {}
        ans = 1000000000
        c = 0
        for i in A:
            # checks if A[i] has occurred previously
            if i in mydict:
                ans = min(ans, c - mydict[i])
                mydict[i] = c
            else:
                mydict[i] = c
            c = c + 1
        if ans == 1000000000:
            ans = -1
        return ans