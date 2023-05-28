# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None
import sys
sys.setrecursionlimit(10**6)
class Solution:
    # @param A : root node of tree
    # @return an integer
    def solve(self, A):

        def sizeOfTree(node):
            if node == None:
                return 0
            ls = sizeOfTree(node.left)
            rs = sizeOfTree(node.right)
            return ls+rs+1
        return sizeOfTree(A)
