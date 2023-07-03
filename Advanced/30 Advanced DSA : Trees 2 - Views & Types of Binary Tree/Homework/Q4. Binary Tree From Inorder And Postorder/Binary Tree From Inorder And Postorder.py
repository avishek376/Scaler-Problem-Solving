# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None
import sys

sys.setrecursionlimit(10 ** 5)


class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return the root node in the tree
    def buildTree(self, A, B):

        postOrder = B
        inOrder = A
        n = len(A)
        postStart = inStart = 0
        postEnd = inEnd = n - 1
        hmap = {}
        for i in range(n):
            hmap[inOrder[i]] = i

        def constructTree(postOrder, postStart, postEnd, inOrder, inStart, inEnd):
            if postStart > postEnd and inStart > inEnd:
                return
            node = TreeNode(postOrder[postEnd])

            idx = hmap[node.val]

            count = idx - inStart

            node.left = constructTree(postOrder, postStart, postStart + count - 1, inOrder, inStart, idx - 1)
            node.right = constructTree(postOrder, postStart + count, postEnd - 1, inOrder, idx + 1, inEnd)

            return node

        return constructTree(postOrder, postStart, postEnd, inOrder, inStart, inEnd)
