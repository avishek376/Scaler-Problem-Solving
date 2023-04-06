class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        mystr = ""
        for i in A:
            mystr += chr(ord(i)^(1<<5))
        return mystr

