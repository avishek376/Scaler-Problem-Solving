In HashMap where we can maintain count of all keys and number of distinct keys, then we just have to reduce count of key A[i] and increasing count of A[i+k]. If count of some key has been reduced to zero, we need to remove that key.

All operations that we have said a constant time in it.
    
    TC: O(N)
    SC: O(N)