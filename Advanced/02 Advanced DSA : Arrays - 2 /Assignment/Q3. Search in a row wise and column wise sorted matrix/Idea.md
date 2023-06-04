We search traversing from the top right corner of the matrix.
1) Check if the current element is greater than B,
then exclude the current column and move to the left column.
2) Check if the current element is less than B, then exclude the 
current row and move to the bottom row.
3) If the current element if equal to B, then the final answer will
be due to the leftmost occurence of B in the current row.


    TC : O(N + M)
    SC : O(1)