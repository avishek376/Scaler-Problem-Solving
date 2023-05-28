Traverse the tree using recursion and if we encounter the left leaf then add the node value in the result.

If both the left and right child of the node is empty and node is the left child of its parent then node is called left leaf node.

Corner Case: If there is only root of the tree, it is not considered as left leaf node.

    TC :O(N)
    SC :O(H)/ <=O(N)
    H : is height of tree