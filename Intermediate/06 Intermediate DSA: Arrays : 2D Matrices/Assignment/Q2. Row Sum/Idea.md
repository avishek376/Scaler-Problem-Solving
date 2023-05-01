Iterate the 2D matrics row-wise and store the sum.
We can iterate the matrix in a row major manner.
For each row we can store its sum in a variable,
and once the sum has been computed for that row,
we can store it in an array, which we finally return as the answer.

    TC: O(N^2)
    SC: O(N)