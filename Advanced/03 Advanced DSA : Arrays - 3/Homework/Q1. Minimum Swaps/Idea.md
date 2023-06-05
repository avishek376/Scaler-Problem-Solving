First, count the number of elements <= B. Let the count comes out to be X.

Create a window of first X elements. To find the number of swaps to bring all elements <= B together in the first window,
you just need to find count of elements > B in first window.
So, count of swaps required in 1 window = count of elements greater than B in that window.

For every window, find the count of elements greater than B, using sliding window technique.

    TC: O(N)
    SC: O(1)