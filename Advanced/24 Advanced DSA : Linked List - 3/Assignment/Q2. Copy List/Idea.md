There are 2 approaches to solving this problem.

**Approach 1: Using hashmap.**

1) Create a new linked list B by traversing the original linked list A and creating a new node for each node in A.
2) While traversing A, create a hash map where the keys are the nodes in A and the values are the corresponding nodes in B.
3) Traverse A again, and for each node in A, use the hash map to find the corresponding node in B. Then, update the next pointer of the current node in B to the corresponding node’s next pointer in A, and update the random pointer of the current node in B to the corresponding node’s random pointer in A.
4) Return the head of the copied linked list B.

**Approach 2 : Using 2 traversals of the list.**

1) Traverse the original linked list A and create a new node A’ for each existing node A and join them together. For example, if the original list is A->B->C, then the new list will be A->A’->B->B’->C->C’.
2) Traverse the new list and copy the random links. For each new node A’, set its random pointer to the corresponding node’s next pointer in the original list. That is, A’.random = A.random.next.
3) Detach the new list from the original list by updating the next pointers. Traverse the new list again and set each node’s next pointer to its next next pointer. For example, if the current node is A’, then A’.next = A’.next.next. Also, set each node’s original next pointer to its original next pointer by setting A.next = A.next.next.
4) Return the head of the new list, which is the second node in the list since the first node is a dummy node.


    TC: O(N)
    SC: O(1)