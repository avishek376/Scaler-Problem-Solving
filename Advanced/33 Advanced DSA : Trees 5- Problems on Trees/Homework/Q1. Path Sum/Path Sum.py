# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return an integer
    def hasPathSum(self, A, B):
        def pathSum(node, summ):

            if not node:
                return 0
            summ -= node.val

            if node.left == None and node.right == None:
                if summ == 0:
                    return 1

            return (pathSum(node.left, summ) or pathSum(node.right, summ))

        return pathSum(A, B)


