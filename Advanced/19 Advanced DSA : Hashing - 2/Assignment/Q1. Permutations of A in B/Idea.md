The main observation required to solve this problem is every permutation of a string will have the same number of characters, and the frequency of each character in every permutation will be identical.

So first, we can create a hash map of size 26 to count the frequency of each character in A.
After that, we can create another hash map of size 26 to count the frequency of each character in the first window of size N (length of A) in B, then slide through all windows, and when both hashes are identical, we can say we found a permutation of A in B as a substring.

Alternate Solution:
We can also keep track of how many alphabets have different frequencies in A and in windows of B. This way, we can solve the problem in O(N) instead of O(26 * N)


    TC: O(N)
    SC: O(1)