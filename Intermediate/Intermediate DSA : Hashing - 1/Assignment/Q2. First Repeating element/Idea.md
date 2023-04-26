We can optimize the solution using Hashing.

We can Use Hashing to solve this in average O(n) time.

The idea is to traverse the given array stored all the elements in hashmap making frequency count.
(Make a frequency count hashmap).

traverse upto array length and check which index val is having more repeatation more than 1
return that index.

    TC: O(N)
    SC: O(N)