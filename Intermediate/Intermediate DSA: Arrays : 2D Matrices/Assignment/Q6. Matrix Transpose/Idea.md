The (i, j)th element in the input array (where i is the row and j is the column) is going to be at (j, i) in the answer matrix.
Initialize an answer list.
Run a inner loop from j = 1 to j = N, and append A[j][i] to temp,
Now append temp to the answer list.
If the size of the input matrix is (N x M), then the answer matrix will have a size of (M x N).
Return the updated answer matrix.
    
    TC: O(M*N)
    Sc: O(M*N)