# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : root node of tree
    # @return an integer
    def isSameTree(self, A, B):

        def inOrderMorrisTraversal(node):
            inOrderList = []
            if not node:
                return inOrderList
            while node:

                if node.left == None:
                    inOrderList.append(node.val)
                    node = node.right
                else:
                    nodeNext = node.left
                    while nodeNext.right != None and nodeNext.right != node:
                        nodeNext = nodeNext.right

                    if nodeNext.right == None:
                        nodeNext.right = node
                        node = node.left
                    else:
                        nodeNext.right = None
                        inOrderList.append(node.val)
                        node = node.right
            return inOrderList

        # firstBT = inOrderMorrisTraversal(A)
        # secondBT = inOrderMorrisTraversal(B)

        if inOrderMorrisTraversal(A) == inOrderMorrisTraversal(B):
            return 1
        return 0


