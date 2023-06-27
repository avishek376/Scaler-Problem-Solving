N^2 solution time complexity can also pass.
We iterate through the given a linked list and one by one reverse every prefix of the linked list from the left.
After reversing a prefix, we find the longest common list beginning from reversed prefix
and the list after the reversed prefix.

    TC: O(N^2)
    SC: O(1)