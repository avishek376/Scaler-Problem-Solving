Traverse the tree with the help of recursion and keep track of the maximum so far.

When arriving at a node, first find the answer for the left sub-tree, if it exists; then find the answer for the right sub-tree; Our current answer is the sum of both ans. But if the current node value is greater than max so far, we increment the answer.

    TC :O(N)
    SC :O(H)/ <=O(N)
    H : is height of tree