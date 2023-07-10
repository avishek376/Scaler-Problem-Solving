# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
	# @param A : root node of tree
	# @return a list of integers
    def inorderTraversal(self, A):
        node = A
        inOrderList = []
        if not node:
            return inOrderList
        while node:
            if node.left == None:
                inOrderList.append(node.val)
                node = node.right
            else:
                nextNode = node.left

                while nextNode.right != None and nextNode.right != node:
                    nextNode = nextNode.right

                if nextNode.right == None:
                    nextNode.right = node
                    node = node.left
                else:
                    nextNode.right = None
                    inOrderList.append(node.val)
                    node = node.right
        return inOrderList


