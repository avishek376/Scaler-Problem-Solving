Approach 1:

Use a HashMap to store the first array, then check each second array element and see if it is in the map.
Note that since we need to output all repeated elements, we also need to count the occurrence of each array element in the map and consume it when we compare it with the second array.
    
    TC: O(N+M)
    SC: O(min(N, m))

Approach 2:
Sort the two arrays and iterate over to find out the intersections. So the overall time complexity is bounded by O(n logn), where n is the length of the longer array.
The main body of the loop is bounded by O(m + n).