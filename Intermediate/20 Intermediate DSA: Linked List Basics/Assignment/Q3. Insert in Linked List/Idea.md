There are three types of insertion possible:-
1) Insert at head - The new node becomes the new head and the next of the 
new node points towards the old head.
2) Insert at tail - The next of the current tail will point toward the new node
3) Insert at any other node - Traverse to the required position, the next of the previous
node should point towards new node and the next of the new node should point towards the
old next of the previos node.


    
    TC : O(N)
    SC : O(1)