
# @param root: ListNode
# @return ListNode
def flatten(root):
    # This function takes a linked list where every node represents a linked list
    # and contains two pointers of its type:
    # - Pointer to next node in the main list (right pointer)
    # - Pointer to a linked list where this node is head (down pointer). All linked lists are sorted.
    # It recursively flattens the linked list into a single list, where down pointer links nodes of the flattened list.
    # The flattened linked list is also sorted.

    def merge(x, y):
        # This function takes two linked list nodes as input and merges them into a sorted linked list
        #  with the down pointers connecting to the child nodes.
        # It recursively traverses the linked lists and merges the nodes.
        if x is None:
            return y
        if y is None:
            return x
        if x.val < y.val:
            ans = x
            ans.down = merge(x.down, y)
        else:
            ans = y
            ans.down = merge(y.down, x)

        return ans

    x = root

    if x is None or x.right is None:
        return x

    return merge(x, flatten(x.right))