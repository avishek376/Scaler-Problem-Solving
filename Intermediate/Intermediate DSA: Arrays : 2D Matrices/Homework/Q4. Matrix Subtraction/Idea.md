1) To subtract the two given matrices we have to subtract their corresponding elements. For example, C[i][j] = A[i][j] - B[i][j].
2) Traverse both matrices row wise(first all elements of a row, then jump to next row) using two nested loops.
3) For every element A[i][j], subtract it with corresponding element B[i][j] and store the result in difference matrix at C[i][j].

    
    TC: O(N^2)
    SC: O(1)