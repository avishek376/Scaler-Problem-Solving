1)One idea is to create new string, iterate A in reverse order
store each character in the new string.


2)To solve the problem without using extra memory, we can traverse
the string till half of its length, and then swap the ith and n - i - 1th characters
where n is the length of the string

    
    TC: O(N)
    SC: O(1)