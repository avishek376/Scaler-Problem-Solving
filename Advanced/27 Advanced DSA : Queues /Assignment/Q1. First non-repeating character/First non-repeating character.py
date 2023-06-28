from collections import deque


class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        q = deque()
        hm = {}
        str = ""
        for i in range(len(A)):
            if A[i] in hm:
                hm[A[i]] += 1
            else:
                hm[A[i]] = 1
            q.append(A[i])

            while len(q) > 0 and hm.get(q[0]) > 1:
                q.popleft()
            else:
                if len(q) > 0:
                    str += q[0]
                else:
                    str += "#"

        return str
