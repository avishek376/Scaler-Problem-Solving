class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        stck = []
        for x in A:
            if len(stck) > 0:
                if x in ["(","{","["]:
                    stck.append(x)
                if x == ")":
                    curr = stck.pop()
                    if curr != "(":
                        return 0
                elif x == "}":
                    curr = stck.pop()
                    if curr != "{":
                        return 0
                elif x == "]":
                    curr = stck.pop()
                    if curr != "[":
                        return 0
            else:
                stck.append(x)
        if len(stck)!=0:
            return 0
        else:
            return 1
