**Approach**

So just recursively traverse the BST , if current node value is greater than both B and C, 
then the LCA lies in the left subtree of the current node. If it is smaller than both B and C, 
then the LCA lies on the right subtree. Otherwise, the current node is the LCA

    TC : O(H)
    SC : O(H),where H is the height of the BST