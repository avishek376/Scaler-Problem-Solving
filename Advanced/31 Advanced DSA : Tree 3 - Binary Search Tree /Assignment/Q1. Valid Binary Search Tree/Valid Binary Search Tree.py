# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def isValidBST(self, A):
        minv = float('-inf')
        maxv = float('inf')

        def checkBST(node, minv, maxv):

            if not node:
                return True
            if node.val < minv or node.val > maxv:
                return False

            l = checkBST(node.left, minv, node.val - 1)
            if l == 0:
                return 0
            r = checkBST(node.right, node.val + 1, maxv)
            if r == 0:
                return 0

            return 1

        return checkBST(A, minv, maxv)