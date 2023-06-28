from collections import deque


class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def slidingMaximum(self, A, B):
        q = deque()

        lst = []
        # for the first window
        for i in range(B):
            while len(q) > 0 and q[-1] < A[i]:
                q.pop()
            q.append(A[i])
        lst.append(q[0])

        for i in range(B, len(A)):
            while len(q) > 0 and q[-1] < A[i]:
                q.pop()
            q.append(A[i])

            if q[0] == A[i - B]:
                q.popleft()
            lst.append(q[0])
        return lst