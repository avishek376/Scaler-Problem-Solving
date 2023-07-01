Recursive call would look something like this : 

      postorderprint(root->left);
      postorderprint(root->right);
      print(root->val);

    TC: O(N)
    SC: O(N)