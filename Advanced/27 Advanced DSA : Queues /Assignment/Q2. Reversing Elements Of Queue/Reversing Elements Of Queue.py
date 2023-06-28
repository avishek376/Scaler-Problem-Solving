from collections import deque


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        # Initializing a Queue
        q = deque()
        # inserting ele. in Queue
        for i in A:
            q.append(i)

        # delete first B ele.from Queue and insert them in Stack
        stck = []
        for i in range(B):
            stck.append(q.popleft())

        # deleting all ele.from Stack and insertin Queue
        for i in range(B):
            q.append(stck.pop())

        # Insert first N-B ele from Queue and insert in same Queue
        for i in range(len(q) - B):
            q.append(q.popleft())
        return q
