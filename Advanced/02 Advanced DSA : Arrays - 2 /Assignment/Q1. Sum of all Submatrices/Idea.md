Let us suppose the index of an element be (X, Y) in 0 based indexing, then the number of submatrices Sub(x,y) for this
element can be given by the formula Sub(x, y) = (X + 1) * (Y + 1) * (N – X) * (N – Y) . This formula works because we
just have to choose two different positions on the matrix that will create a submatrix that envelopes the element. Thus,
for each element, ‘sum’ can be updated as sum += Sub(x,y) * A[x][y].

    This line calculates the contribution of the element at position (i, j) to the sum of all submatrices. Here's a breakdown of each part of the expression:
    
    (i + 1) and (j + 1): These terms represent the number of ways we can choose the row and column positions to form the top-left corner of a submatrix. Since indexing starts from 0, we add 1 to both i and j to account for the number of valid choices of rows and columns. For example, if i = 0 and j = 0, (i + 1) and (j + 1) would be 1, indicating that there is 1 way to choose the top-left corner.
    (rows - i) and (cols - j): These terms represent the number of ways we can choose the bottom-right corner of the submatrix relative to the current position (i, j). Subtracting i from rows and j from cols gives us the number of rows and columns remaining in the matrix after choosing (i, j) as the top-left corner. For example, if there are 3 rows in total and i = 0, (rows - i) would be 3, indicating that there are 3 possible choices for the height of the submatrix.
    matrix[i][j]: This term represents the value of the element at position (i, j) in the original matrix. Multiplying this value by the number of ways we can choose the top-left and bottom-right corners gives us the total contribution of this element to the sum of all submatrices.
    By multiplying these terms together, we get the contribution of the current position (i, j) to the sum of all submatrices. This contribution is then added to the total_sum variable, which accumulates the sum of contributions from all elements in the matrix.

More Formally, Number of ways to choose from top-left elements (X + 1) * (Y + 1)
Number of ways to choose from bottom-right elements (N - X) * (N - Y)

    TC: O(N^2)
    SC: O(1)