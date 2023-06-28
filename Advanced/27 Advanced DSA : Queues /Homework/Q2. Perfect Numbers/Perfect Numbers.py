from collections import deque
class Solution:
    # @param A : integer
    # @return a strings
    def solve(self, A):
        q = deque()
        q.append("1")
        q.append("2")
        ans = ""

        for i in range(A):
            if len(q)>0:
                curr = q.popleft()
                value1 = curr+"1"
                value2 = curr+"2"
                q.append(value1)
                q.append(value2)
                ans = curr+curr[::-1]
        return ans