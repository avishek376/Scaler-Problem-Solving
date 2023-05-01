We can iterate the matrix in a column major manner.
For each column we can store its sum in a variable,
and once the sum has been computed for that column,
we can store it in an array, which we finally return as the answer.
Iterate the 2D matrics column-wise & store the sum.

    TC: O(N^2)
    TC: O(N)