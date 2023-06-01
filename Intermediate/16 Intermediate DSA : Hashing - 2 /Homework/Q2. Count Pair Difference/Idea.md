We can use a hash-map and store the elements of the array
as the key and its frequency as the value. 
We traverse the array from left to right.
Now, for every element we count the number of occurences of 
A[i] + B and A[i] - B to its left side and increment that to our answer.
    
    TC : O(N)
    SC : O(N)