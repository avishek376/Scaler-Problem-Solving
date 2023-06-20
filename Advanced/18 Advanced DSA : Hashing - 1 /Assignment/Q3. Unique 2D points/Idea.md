Use a hash set (or a dictionary/map in some languages) to keep track of the unique points.
For each point in the array, we add it to the set if it is not already in the set.
At the end, the size of the set will give us the number of unique points.

    TC - O(N)
    SC - O(N)