# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def solve(self, A):

        def leftTreeSum(root):
            if not root:
                return 0

            if root.left != None and root.left.left == None and root.left.right == None:
                return root.left.val + leftTreeSum(root.right)
            else:
                return leftTreeSum(root.left) + leftTreeSum(root.right)

        return leftTreeSum(A)


'''
# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def solve(self, A):
        summ = 0
        leftCheck = False
        def leftTreeSum(node,leftCheck,summ):
            if node == None:
                return 0 
            if node.left == None and node.right == None and leftCheck == True:
                summ += node.val
            return summ+leftTreeSum(node.left,True,summ)+leftTreeSum(node.right,False,summ)
            
        return leftTreeSum(A,leftCheck,summ)
'''