# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None
import sys

sys.setrecursionlimit(10 ** 5)


class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def recoverTree(self, A):
        firstNode = secondNode = None
        prev = TreeNode(-1)

        def inOrder(curr):
            nonlocal prev, firstNode, secondNode
            if not curr:
                return

            inOrder(curr.left)

            if prev != None and prev.val > curr.val and firstNode == None:
                firstNode = prev
                secondNode = curr
            elif prev != None and prev.val > curr.val:
                secondNode = curr

            prev = curr

            inOrder(curr.right)

        inOrder(A)
        return [secondNode.val, firstNode.val]



