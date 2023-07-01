Recursive call would look something like this :

    print(root->val);
    preorderprint(root->left);
    preorderprint(root->right);


    TC: O(N)
    SC: O(N)