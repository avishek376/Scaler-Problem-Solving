If the two string A and B are anagrams, then the frequncy of each
character in both the strings must be same. So we can keep an array of 
size 26 to calculate the frequency of each characters for each of the strings.
Finally, we will compare the two frequency arrays. If they are equal, then the
strings are anagrams.

    TC : O(N)
    SC : O(26)