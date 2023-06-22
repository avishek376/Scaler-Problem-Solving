1) How to check if loop is present in the given linkedlist or not ->
Take two pointers - slow and fast and initialize them with head of linkedlist.
2) Keep moving slow by one step and fast by two steps.
If at any point slow and fast are meeting, that means, loop is detected.
3) After that, to find the first node in the loop, re-initialize just slow with head of linkedlist.
4) Keep moving slow and fast both by one step only. They will meet again and they will meet at first node of the loop.
Finally, break the loop.
Note - (Check the video solution for the proof).


    TC: O(N)
    SC: O(1)