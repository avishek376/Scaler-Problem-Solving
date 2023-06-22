One way is to traverse the whole linked list and calculate the length and then traverse half the length to find the middle element.

We can do it in one traversal by maintaining a slow and fast pointer.

The fast pointer moves twice as the slow pointer does. When the fast pointer is at the end of the linked list, the slow pointer will point to the middle element.

Return the element at which the slow pointer points.

    TC: O(N)
    SC: O(1)