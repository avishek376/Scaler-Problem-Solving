You can use hashing to solve this question.

For each character in A, store the corresponding character in B.

If there is a contradiction in the mapping, then you can directly return the value 0.
If the character wasn't already present, then insert it into the character map.
Also, the lengths of the string need to be equal to be isomorphic.

    TC: O(N)
    SC: O(N)