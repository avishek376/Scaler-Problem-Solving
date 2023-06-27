To check palindrome, we just have to reverse the latter half of the linked list, and then we can, in (n/2) steps total can compare if all elements are the same or not.
For finding the midpoint, first, we can in O(N) traverse the whole list and calculate the total number of elements.
Reversing is again O(N).

    TC: O(N)
    SC: O(1)