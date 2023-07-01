Recursive call would look something like this :

    inorderprint(root->left)
    print(root->val)
    inorderprint(root->right)

    TC: O(N)
    SC: O(N)