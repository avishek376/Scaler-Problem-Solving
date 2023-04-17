We have to maintain a state indicating which direction we are traversing to
( left-> right, right->bottom, bottom->left, left->top ).
Observe that in each direction either row or a column remains constant.
    
    TC: O(N^2)
    SC: O(N^2)