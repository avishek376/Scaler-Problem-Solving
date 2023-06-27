We can use a stack to find the next greater element.

Push the first element in the stack.
Pick rest of the elements one by one and follow the following steps in loop
Mark the current element as next.
If stack is not empty, compare top element of stack with next.
If next is greater than the top element, Pop element from stack. Next is the next greater element for the popped element.
Keep popping from the stack while the popped element is smaller than next. Next becomes the next greater element for all such popped elements.
Finally, push the next in the stack.
After the loop in step 2 is over, pop all the elements from stack and print -1 as next element for them.

    TC: O(N)
    SC: O(N)