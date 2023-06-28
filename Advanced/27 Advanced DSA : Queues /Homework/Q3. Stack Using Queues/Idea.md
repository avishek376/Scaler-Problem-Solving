In order to implement stack using queues, we need to maintain two queues q1 and q2.

Algorithm:

1) For push:
The new element is always added to the rear of queue q1 and it is kept as top stack element

2) For pop:
We need to remove the element from the top of the stack. This is the last inserted element in q1. Because queue is FIFO (first in - first out) data structure, the last inserted element could be removed only after all elements, except it, have been removed. For this reason we need to maintain additional queue q2, which will serve as a temporary storage to enqueue the removed elements from q1. The last inserted element in q2 is kept as top. Then the algorithm removes the last element in q1. We swap q1 with q2 to avoid copying all elements from q2 to q1.

3) For empty:
Queue q1 always contains all stack elements, so the algorithm checks q1 size to return if the stack is empty.

4) For top:
The top element is the rear element of q1. We will do the same operations done in pop except for the operation of removing the element.


    TC: O(N)
    SC: O(N)