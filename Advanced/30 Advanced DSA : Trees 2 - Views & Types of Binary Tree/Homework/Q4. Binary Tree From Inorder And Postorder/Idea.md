Focus on the postorder traversal, to begin with.
The last element in the traversal will definitely be the root.
Based on this information, can you identify the left subtree and right subtree elements? ( Hint: Focus on inorder traversal and root information )

Once you do that, your problem has now been reduced to a smaller set. Now you have the inorder and postorder traversal for the left and right subtree, and you need to figure them out.
Divide and conquer.

    TC: O(N)
    SC: O(H), H is height of Tree