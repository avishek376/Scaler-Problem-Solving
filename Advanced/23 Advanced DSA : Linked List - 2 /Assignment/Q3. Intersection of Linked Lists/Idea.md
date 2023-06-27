**Approach-1**

1) Join the smaller list end to head of the longer list
2) Now perform floyd's algo with slow and fast pointer
    

    TC: O(N)
    SC: O(1)

**Approach-2**
1) Find the length of each list.
2) Difference of their length will be the distance from intersection to each other.
3) Now process that much length(difference length) in bigger list. Means,
start a pointer and reach to difference length in bigger list.
4) Now traverse both of the list to get the intersection point


    TC: O(N)
    SC: O(1)