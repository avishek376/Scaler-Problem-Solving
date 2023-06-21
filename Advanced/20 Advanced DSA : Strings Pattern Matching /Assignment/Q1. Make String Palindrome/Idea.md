**Approach**

1) Each index of the LPS array contains the longest prefix, which is also a suffix. 
2) Now take the string and reverse of a string and combine them with a sentinel character in between them and compute the LPS array of this combined string.
3) Now take the last value of the LPS array and subtract it from the length of the original string. This will give us the minimum number of insertions required at the beginning of the string.

    TC: O(N)
    SC: O(N)