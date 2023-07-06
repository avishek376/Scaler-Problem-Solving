# Definition for a  binary tree node
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
from collections import deque


class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):

        if not root:
            return

        q = deque()
        q.append(root)

        while q:
            Right_Node = None
            for _ in range(len(q)):
                cur_node = q.popleft()

                if cur_node:
                    cur_node.next = Right_Node
                    Right_Node = cur_node

                if cur_node.right:
                    q.append(cur_node.right)

                if cur_node.left:
                    q.append(cur_node.left)

        return root


