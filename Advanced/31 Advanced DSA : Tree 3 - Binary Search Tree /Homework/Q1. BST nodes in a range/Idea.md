The idea is to traverse the given binary search tree starting from the root.
For every node being visited, check if this node lies in range,
if yes, then add 1 to the result and recur for both of its children.
If the current node is smaller than the low value of the range, then recur for the right child; else recur for the left child.


    TC: O(N)
    SC: O(H)