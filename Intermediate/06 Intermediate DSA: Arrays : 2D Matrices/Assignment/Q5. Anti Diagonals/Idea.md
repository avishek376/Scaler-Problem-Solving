Let’s look at how the coordinates change when you move from one element to the other in the anti-diagonal.
With every movement, the row increases by one, and the column decreases by one ( or in other words, (1, -1) gets added to the current coordinates).
Now, all we need to know is the start ( or the first element ) in each diagonal.
After finding each first or start element in each diagonal, we can use it to print the matrix.
    
    TC: O(N^2)
    SC: O(N)