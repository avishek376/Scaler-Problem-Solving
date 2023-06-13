We can use two loops and calculate the number of pairs that satisfy the condition, 
but the time complexity will be O(N^2), which will not work in the worst case. 

So we can think of a better solution, i.e., using merge sort.
 
We will do a usual merge sort, but before calling the merge function, 
we will calculate the number of pairs using two pointers, 
considering that the two arrays are sorted individually. 

Likewise, we will do this till our mergesort ends, i.e., the array becomes sorted.
    
    TC: O(NlogN)
    SC: O(N)