# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None
from collections import deque


class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def solve(self, A):
        q = deque()
        hmap = {}
        maxv = -10 ** 9
        minv = 10 ** 9
        q.append((A, 0))

        while q:

            curr = q.popleft()
            maxv = max(curr[1], maxv)
            minv = min(curr[1], minv)

            hmap[curr[1]] = curr[0].val

            if curr[0].left is not None:
                q.append((curr[0].left, curr[1] - 1))

            if curr[0].right is not None:
                q.append((curr[0].right, curr[1] + 1))
        lst = []
        for i in range(minv, maxv + 1):
            lst.append(hmap[i])

        return lst
