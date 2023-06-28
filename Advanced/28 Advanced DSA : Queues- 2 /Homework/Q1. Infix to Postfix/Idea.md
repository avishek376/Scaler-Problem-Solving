Given the algorithm below, we have used a stack to keep the operators in the precedence order.

Algorithm:

1) Scan the infix expression from left to right. 
2) If the scanned character is an operand, output it.
Else, 
3) 3.1 If the precedence of the scanned operator is greater than that of the operator in the stack(or the stack is empty, or the stack contains a ‘(‘ ), push it. 
4) Else, Pop all the operators from the stack which are greater than or equal to in precedence than that of the scanned operator. After doing that, Push the scanned operator to the stack. (If you encounter parenthesis while popping, stop there and push the scanned operator in the stack.)
5) If the scanned character is an ‘(‘, push it to the stack. 
6) If the scanned character is an ‘)’, pop the stack and output it until a ‘(‘ is encountered, and discard both the parenthesis. 
7) Repeat steps 2-6 until infix expression is scanned. 
8) Print the output 
9) Pop and output from the stack until it is not empty.



    TC: O(N)
    SC: O(N)