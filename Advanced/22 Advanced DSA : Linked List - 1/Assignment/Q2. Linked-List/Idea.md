We will maintain the head of the LinkedList.

For Insert operation - Firstly, we will traverse the list and keep two pointers, current and previous.
So if the position is 1, we will add the node in the beginning and update the head.
Otherwise, we will traverse the list up to the desired position and add the node by making the current node, the next node of the
newly added node, and the next node of the previous node will be the newly added node.

For Print LinkedList Operation - We will print the data of all the nodes by traversing through the list and stop
when our current pointer becomes null.

For Delete LinkedList Operation - We will traverse the list up to the desired position and keep track of two pointers, current and previous.
If the position is 1, we will make the new head of the list the next element of the last head.
Otherwise, make the next element of the previous node the next element of the current node. At last, free the pointer of the current node.

    TC: O(N)
    SC: (1)