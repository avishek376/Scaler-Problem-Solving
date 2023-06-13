Sort the list of these points with respect to the distance from the origin. 
We can do this with the help of a comparator function, which takes two elements of the array as input 
and returns which one will be smaller than the other. So basically, it takes care of the comparison process.

After the list is sorted, take the first B elements from the list and create a new list and return it. 
Think of calculating the Euclidean distance and storing it efficiently.

    TC: O(N log N)
    SC: O(N)



**2Nd Approach:** 

By Min-Heap you can perform the same by

    TC: O(N)
    SC: (N)