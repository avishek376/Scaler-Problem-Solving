A simpler approach, O(N2) time and O(1) space:

In fact, we could solve it in O(N2) time without any extra space.

We observe that a palindrome mirrors around its center. Therefore, a palindrome can be expanded from its center, and there are only 2N-1 such centers.

You might be asking why there are 2N-1 but not N centers?

The reason is that the center of a palindrome can be in between two letters.

Such palindromes have even number of letters (such as “abba”) and their center are between the two ‘b’s.

Since expanding a palindrome around its center could take O(N) time, the overall complexity is O(N2).
    
    TC: O(N^2)
    SC: O(N)