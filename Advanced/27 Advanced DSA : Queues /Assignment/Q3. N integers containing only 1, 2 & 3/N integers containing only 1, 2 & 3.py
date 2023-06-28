from collections import deque


class Solution:
    # @param A : integer
    # @return a list of integers
    def solve(self, A):
        q = deque()
        lst = []
        q.append("1")
        q.append("2")
        q.append("3")

        for i in range(A):
            element = q.popleft()  # Pops out the front of the queue
            lst.append(element)

            q.append(element + "1")
            q.append(element + "2")
            q.append(element + "3")

        return lst
