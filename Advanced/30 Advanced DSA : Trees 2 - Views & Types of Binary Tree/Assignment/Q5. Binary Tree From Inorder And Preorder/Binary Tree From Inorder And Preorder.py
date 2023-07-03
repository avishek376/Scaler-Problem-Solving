# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
import sys

sys.setrecursionlimit(10 ** 6)


class Solution:
# @param A : list of integers
# @param B : list of integers
# @return the root node in the tree
    def buildTree(self, A, B):
        preOrder = A
        inOrder = B
        ps = ist = 0
        pe = ien = len(A) - 1

        def searchEle(arr, sindex, eindex, ele):
            for i in range(sindex, eindex + 1):
                if arr[i] == ele:
                    return i
                else:
                    return False

        def constructTree(preOrder, ps, pe, inOrder, ist, ien):

            if ps > pe and ist > ien:
                return

            node = TreeNode(preOrder[ps])

            idx = 0
            for i in range(ist, ien + 1):


                if inOrder[i] == node.val:
                    idx = i
                count = idx - ist

            node.left = constructTree(preOrder, ps + 1, ps + count, inOrder, ist, idx - 1)
            node.right = constructTree(preOrder, ps + count + 1, pe, inOrder, idx + 1, ien)

            return node

        return constructTree(preOrder, ps, pe, inOrder, ist, ien)