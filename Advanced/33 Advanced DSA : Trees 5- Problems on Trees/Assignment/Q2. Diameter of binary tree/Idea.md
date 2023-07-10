First, let’s see how to find the height or maxDepth of a tree:

If the tree is empty, then return 0
Else
(a) Get the max depth of each subtree recursively.

(b) Take the max depth and second max depth of any subtree. Get the max depth of the right subtree recursively, i.e., call height( tree->right-subtree)

(c) Get the max of max depths of left and right subtrees and add 1 to it for the current node.
max_depth = max(max dept of left subtree, max depth of right subtree) + 1

(d) Return max_depth

Diameter of a tree can be calculated by only using the height function, because the diameter of a tree is nothing but maximum value of (left_height + right_height + 1) for each node. So we need to calculate this value (left_height + right_height + 1) for each node and update the result. 


    TC: O(N)
    SC: O(H)