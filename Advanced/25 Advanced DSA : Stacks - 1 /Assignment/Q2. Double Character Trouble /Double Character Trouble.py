class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        stk = []
        for x in A :
            if len(stk) > 0 :
                if stk[-1] == x :
                    stk.pop()
                else :
                    stk.append(x)
            else :
                stk.append(x)
        return ''.join(stk)
