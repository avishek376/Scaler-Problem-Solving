In order to implement queue using stacks, we need to maintain two stacks s1 and s2.

Algorithm:

1) For push: 
The new element is always added to the top of stack s1 and it is kept as rear element 
of the queue.

2) For pop:
We have to remove element in front of the queue. This is the first inserted element 
in the stack s1 and it is positioned at the bottom of the stack because of stack's LIFO 
(last in - first out) policy. To remove the bottom element from s1, we have to pop all 
elements from s1 and to push them on to an additional stack s2, which helps us to store 
the elements of s1 in reversed order. This way the bottom element of s1 will be 
positioned on top of s2 and we can simply pop it from stack s2. Once s2 is empty, 
the algorithm transfer data from s1 to s2 again.

3) For empty:
Both stacks s1 and s2 contain all stack elements, so the algorithm checks s1 and 
s2 size to return if the queue is empty.

4) For peek:
The rear element is the bottom element of s1. We will do the same operations done 
in pop except for the operation of removing the element.


    TC: O(N)
    SC: O(1)