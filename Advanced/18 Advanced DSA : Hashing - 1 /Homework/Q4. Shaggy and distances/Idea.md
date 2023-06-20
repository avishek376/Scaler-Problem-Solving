Idea behind this problem is to use hashing.

Iterate over the the array and for each element if you found that element earlier also
(i.e. stored in hash) then take the distance between them and update the hash with the
current index.
Answer will be minimum of all distances

We are storing the most recent found index of each element because that will be the closest
to the left of the next found index.

    TC : O(N)
    SC : O(N)