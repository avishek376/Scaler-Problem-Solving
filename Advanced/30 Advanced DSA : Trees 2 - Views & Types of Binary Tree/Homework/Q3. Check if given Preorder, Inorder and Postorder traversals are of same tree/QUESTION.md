Given 3 array of integers A, B and C.

A represents preorder traversal of a binary tree.

B represents inorder traversal of a binary tree.

C represents postorder traversal of a binary tree.

Check whether these tree traversals are of the same tree or not. If they are of same tree return 1 else return 0.


Input Format

The arguments given are integer arrays A, B, and C.

Output Format

Return 1 if they are of same tree else return 0.

Constraints

    1 <= length of the array <= 1000
    all arrays are of same length
    1 <= A[i], B[i], C[i] <= 10^9 

For Example

    Input 1:
    
        A = [1, 2, 4, 5, 3]
        B = [4, 2, 5, 1, 3]
        C = [4, 5, 2, 3, 1]
    
    Output 1:
    
        1
    
    Input 2:
    
        A = [1, 5, 4, 2, 3]
        B = [4, 2, 5, 1, 3]
        C = [4, 1, 2, 3, 5]
    
    Output 2:
    
        0