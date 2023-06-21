**Approach**

1) Each index of the LPS array contains the longest prefix, which is also a suffix. 
2) Now take the B string and A string combine them with a sentinel character in between them and compute the LPS array of this combined string.
3) Like string will be string `B@A`
4) Now check the occurrence ,means count for every LPS arr ele where length is same with B string, that many times B occurred in A string.


    TC: O(N)
    SC: O(N)