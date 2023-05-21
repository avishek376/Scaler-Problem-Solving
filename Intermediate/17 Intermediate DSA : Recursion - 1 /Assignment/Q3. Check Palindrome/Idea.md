Consider two indexes i and j, initially at the first and last index of the string, respectively.

If the character at both i and j index is the same, check recursively for i+1, j-1.

We can say that, F(i, j) tell if the string from i to j is palindrome or not:

if(A[i] == A[j])
F(i, j) = F(i+1, j-1)
else
F(i, j) = 0


    TC :O(N)
    SC :O(N)