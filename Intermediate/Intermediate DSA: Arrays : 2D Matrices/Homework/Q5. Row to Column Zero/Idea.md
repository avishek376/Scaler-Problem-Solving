Let's start row wise first. Select rows one by one and make all the elements of that row -1 except which are 0, if any element in that row is 0. Similariy you have to do the same thing for columns.
Now, before returning traverse the matrix and make all the -1 elements 0.

    TC: O(N^2)
    SC: O(N)