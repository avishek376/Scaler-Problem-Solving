If the value of B is zero, then we return the next node pointed
by A.

We need to find the previous node to one which we would delete. Then,
make the next of this node equal to the next of the node to be deleted.

    TC : O(N)
    SC : O(1)