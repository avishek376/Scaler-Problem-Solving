# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None
import sys

sys.setrecursionlimit(10 ** 5)


class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):

        def lca(root, node1, node2):
            while root:
                if root.val > node1 and root.val > node2:
                    root = root.left
                elif root.val < node1 and root.val < node2:
                    root = root.right
                else:
                    return root

        def deapth(root, node):
            dist = 0
            temp = root
            while temp:
                if temp.val < node:
                    temp = temp.right
                    dist += 1
                elif temp.val > node:
                    temp = temp.left
                    dist += 1
                else:
                    break
            return dist

        getLCA = lca(A, B, C)

        return deapth(getLCA, B) + deapth(getLCA, C)