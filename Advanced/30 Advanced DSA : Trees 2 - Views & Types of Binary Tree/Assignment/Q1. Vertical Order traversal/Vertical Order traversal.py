# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None
from collections import deque


class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def verticalOrderTraversal(self, A):
        q = deque()

        hmap = {}
        q.append((A, 0))
        minv = 10 ** 9 + 7
        maxv = -10 ** 9 + 7

        while q:
            curr = q.popleft()
            minv = min(minv, curr[1])
            maxv = max(maxv, curr[1])
            if hmap.get(curr[1]):
                hmap[curr[1]].append(curr[0].val)
            else:
                hmap[curr[1]] = [curr[0].val]

            if curr[0].left != None:
                q.append((curr[0].left, curr[1] - 1))
            if curr[0].right != None:
                q.append((curr[0].right, curr[1] + 1))

        ans = []
        for i in range(minv, maxv + 1):
            ans.append(hmap[i])
        return ans



