The first thing to note is that all you would want to do is modify the next pointers. You don’t need to create new nodes.

At every step, you choose the minimum of the current head X on the 2 lists and modify your answer’s next pointer to X. You move the current pointer on the said list and the current answer.

Corner case,
Make sure that at the end of the loop, when one of the lists goes empty, you do include the remaining elements from the second list into your answer.

    TC: O(N)
    SC: O(1)