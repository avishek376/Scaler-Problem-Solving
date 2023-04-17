For every A[i], we calculate no of elements A[j] 
such that A[j] < A[i] and j < i. 
Similary, we also calculate the no of elements A[j]
such that A[j] > A[i] and  j > i.
Now, the number of triplets with A[i] as the centre is the
product of the above two calculated values. 
We can get this count for all the elements and add their total.

    TC: O(N^2)
    SC : O(1)