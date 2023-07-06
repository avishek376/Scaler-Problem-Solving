1) Find a path from the root to n1 and store it in a vector or array.
2) Find a path from the root to n2 and store it in another vector or array.
3) Traverse both paths till the values in arrays are the same. Return the common element just before the mismatch

Linear solution using recursion :

We traverse from the bottom, and once we reach a node that matches one of the two nodes, we pass it up to its parent. The parent will then test its left and right subtree if each contains one of the two nodes. If yes, then the parent must be the LCA, and we pass its parent up to the root.

    
    TC: O(N)
    SC: O(H)