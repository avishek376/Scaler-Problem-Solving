The naive approach is to generate all possible submatrices from the given matrix and calculate their sum 
and return the maximum sum among them. What is the Time Complexity of this solution?
Time Complexity - O(N^6). This too slow for the given constraints.
Can you optimize this further? Think using Kadane's Algorithm.

Fix starting and ending column of the required sub-matrix say start and end respectively.
Now, iterate each row and add row sum from starting to ending column to sumSubmatrix and insert this in an array. 
After iterating each row, perform Kadane’s Algorithm on this newly created array.
If the sum obtained by applying Kadane’s algorithm is greater than the overall maximum sum, update the overall maximum sum.
In the above step, the row sum from starting to ending column can be calculated in constant time by creating
an auxiliary matrix of size N*M containing the prefix sum of each row.

    TC: O(N^3)
    SC: O(N^2)