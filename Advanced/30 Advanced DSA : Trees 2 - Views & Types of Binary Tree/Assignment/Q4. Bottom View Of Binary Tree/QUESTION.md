Problem Description

Given a Binary Tree A consisting of N integer nodes, you need to print the bottom view from left to right.

A node x is there in output if x is the bottom-most node at its horizontal distance.

Horizontal distance of left child of a node x is equal to horizontal distance of x minus 1, and that of right child is horizontal distance of x plus 1.

Note: If there are multiple bottom-most nodes for a horizontal distance from root, then print the later one in level traversal.



Problem Constraints
    
    0 <= N <= 105



Input Format

First and only Argument represents the root of binary tree A.



Output Format

Return an one-dimensional integer array denoting the bottom view of A from left to right.



Example Input
    
    Input:1
    
                          20
                        /    \
                      8       22
                    /   \      \
                  5      3      25
                        / \      
                      10    14
    Input:2
    
                          20
                        /    \
                      8       22
                    /   \    /   \
                  5      3  4    25
                        / \      
                      10    14
    
    
    Example Output
    
    Output:1
    
     [5, 10, 3, 14, 25]
    
    Output:2
    
     [5, 10, 4, 14, 25]
    

Example Explanation

Explanation:1

Node 5 has a horizontal distance of -2 and it is the bottom-most node at this distance.
Node 10 has a horizontal distance of -1 and it is the bottom-most node at this distance.
Node 3 has a horizontal distance of 0 and it is the bottom-most node at this distance.
Node 14 has a horizontal distance of 1 and it is the bottom-most node at this distance.
Node 25 has a horizontal distance of 2 and it is the bottom-most node at this distance.

Explanation:2

 
 Node 5 has a horizontal distance of -2 and it is the bottom-most node at this distance.
 Node 10 has a horizontal distance of -1 and it is the bottom-most node at this distance.
 Node 3 and Node 4 has a horizontal distance of 0 and they are the bottom-most node at this distance but we will output the one who comes later in level-order traversal so we output 4.
 Similarly for Node 14 and 25