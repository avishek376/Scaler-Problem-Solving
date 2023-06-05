**Method 1- Brute Force:**

A Simple Solution is to consider all possible sub-squares of size B x B in our input matrix and find the one which has the maximum sum.

Time complexity of above solution is O(N^2B^2).
This will timeout for the given constraints.


**Method 2- Efficient Approach:**

The idea is to preprocess the given square matrix. In the preprocessing step, calculate the sum of all vertical strips of size B x 1 in a temporary square matrix stripSum[][].
Once we have the sum of all vertical strips, we can calculate the sum of the first sub-square in a row as the sum of the first B strips in that row, and for the remaining sub-squares, we can calculate the sum in O(1) time by removing the leftmost strip of the previous subsquare and adding the rightmost strip of the new square.
    
    TC: O(N^2)
    SC: O(N^2)