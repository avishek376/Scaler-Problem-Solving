First, let us look at the impossible cases:
1) [() : There is no corresponding closing bracket for an opening bracket.
2) [) : Incorrect closing bracket for an opening bracket.
3) } : No opening bracket for a closed bracket.

Now, we can observe that the earlier a bracket is encountered in the string, the later it is closed.
We can guess that the Stack Data Structure will be used using this observation.

We traverse the given string from the left. If the i-th character is an opening bracket, we push it onto the stack.
If it is a closing bracket, we check for the impossible case 2 and case 3. If they are being violated, then we can simply return 0. Otherwise, we can pop the topmost bracket from the stack.
To check for case 1, if our stack is not empty at the end of our traversal, then we can say that the brackets are not correctly matched.

If all the conditions are fulfilled, then we can return 1.

    TC: O(N)
    SC: O(N)