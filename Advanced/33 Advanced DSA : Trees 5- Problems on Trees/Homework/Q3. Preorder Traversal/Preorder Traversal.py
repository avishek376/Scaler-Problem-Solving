# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def preorderTraversal(self, A):
        curr = A

        preOrderList = []
        while curr:
            if curr.left == None:
                preOrderList.append(curr.val)
                curr = curr.right
            else:
                currNext = curr.left
                while currNext.right != None and currNext.right != curr:
                    currNext = currNext.right
                if currNext.right == None:
                    preOrderList.append(curr.val)
                    currNext.right = curr
                    curr = curr.left
                else:
                    currNext.right = None
                    curr = curr.right
        return preOrderList

