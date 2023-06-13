Problem Description

Given two sorted arrays of integers A and B, sorted in ascending order.

Merge the two arrays A and B into a single array such that it contain all the elements from A and B and it remain sorted at the same time.

Find and return the resultant merged array.



Problem Constraints
    
    1 <= Length of both the arrays <= 105
    1 <= A[i], B[i] <= 109



Input Format

The first argument given is the integer array A.

The second argument given is the integer array B.



Output Format

Return a one-dimensional integer array denoting the resultant merged array.



Example Input

    Input 1:
    
     A = [1, 3, 4]
     B = [2, 5, 6]
    
    Input 2:
    
     A = [2, 5]
     B = [1, 2, 3]
    
    
    Example Output
    
    Output 1:
    
     [1, 2, 3, 4, 5, 6]
    
    Output 2:
    
     [1, 2, 2, 3, 5]
    

Example Explanation

Explanation 1:

 On merging A and B together you get [1, 2, 3, 4, 5, 6]

Explanation 2:

 On merging A and B together you get [1, 2, 2, 3, 5]
 