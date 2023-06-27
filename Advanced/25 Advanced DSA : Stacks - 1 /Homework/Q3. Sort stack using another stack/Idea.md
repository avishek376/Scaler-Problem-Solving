**Approach**
Create a temporary stack say B.

While input stack is not empty:
1. pop an element from input stack calls it x.
2. while the temporary stack is not empty and top of the temporary stack is greater than x pop from the temporary stack and push it into input stack.
3. push x in the temporary stack.

The sorted numbers are in the temporary stack.

    TC: O(N^2)
    SC: O(N)