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
    def lca(self, A, B, C):
        def findPath(node, path, key):
            if not node:
                return False

            path.append(node.val)
            if node.val == key:
                return True

            # Check if key is found in left or right sub-tree
            if ((node.left != None and findPath(node.left, path, key)) or
                    (node.right != None and findPath(node.right, path, key))):
                return True

            path.pop()
            return False

        path1 = []
        path2 = []
        if (not findPath(A, path1, B) or not findPath(A, path2, C)):
            return -1

        i = 0
        while (i < len(path1) and i < len(path2)):
            if path1[i] != path2[i]:
                break
            i += 1
        return path1[i - 1]

