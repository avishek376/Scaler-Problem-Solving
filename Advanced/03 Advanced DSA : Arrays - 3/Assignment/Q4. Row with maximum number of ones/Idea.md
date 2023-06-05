We will start iterating from the top-right of the matrix.
We check for all rows from top to bottom and store the maximum
answer so far.
For every row, we only search from the left of the index of maximum answer so far. 
    
    TC : O(M + N)
    SC : O(1)