Obviously, since we do not have back pointers, reaching the end node and then making our way back is not an option.

There are 2 approaches :
1) Find out the length of the list in one go. Then you know the number of the node to be removed. Traverse to the node and remove it.
2) Make the first pointer go n nodes. Then move the second and first pointer simultaneously. This way, the first pointer is always ahead of the second pointer by n nodes. So when the first pointer reaches the end, you are on the node to be removed.


    TC: O(N)
    SC: O(1)