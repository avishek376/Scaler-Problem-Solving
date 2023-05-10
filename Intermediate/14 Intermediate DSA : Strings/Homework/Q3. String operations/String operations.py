class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        A += A
        b = ""
        n = len(A)
        for i in A:
            if i>= 'a' and i<= 'z':
                if i== 'a' or i== 'e' or i== 'o' or i== 'i' or i== 'u':
                    b+='#'
                else:
                    b += i
        return b