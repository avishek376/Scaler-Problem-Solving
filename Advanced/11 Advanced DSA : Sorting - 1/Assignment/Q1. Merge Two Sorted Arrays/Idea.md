Use of additional space is allowed.
So, maybe you should try collecting the output in a separate array.

Note:
You need two pointers at the head of each array,
and you need to compare the values at the head of the arrays to get the current minimum.

Since A is sorted, all values after the pointer are going to be bigger.
Since B is sorted, all values after the pointer are going to be bigger.

All values before the pointer have already been put in the result array.

Corner cases:

What if pointer 1 reaches the end of the array first?
What if pointer 2 reaches the end of the array first?

If pointer 1 reaches the end we can just keep on putting the elements from B
in the result array while the pointer 2 does not reach the end.
The same process goes for if pointer 2 reaches the end.

    TC: O(N)
    SC: O(N)