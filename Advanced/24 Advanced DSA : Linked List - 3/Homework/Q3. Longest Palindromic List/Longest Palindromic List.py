# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return an integer
    def solve(self, A):
        # This function takes two linked list nodes as input and counts the number of consecutive nodes
        # with the same value in both linked lists.
        def count(x, y):
            count = 0
            # Keep looping while both linked lists have nodes and the current node in each linked list has the same value.
            while x and y:
                if x.val != y.val:
                    break
                else:
                    count+=1
                # Move to the next node in each linked list.
                x = x.next
                y = y.next
            return count
        ans=0
        prev=None
        x=A
        while x:
            nxt=x.next
            x.next=prev

            # Check for odd palindromes , the middle emnt will not b checked
            ans = max(ans, 2 * count(prev, nxt) + 1)

            # Check for even palindromes , both sides curr and curr next will b checked
            ans = max(ans, 2 * count(x, nxt))

            # Move to the next node in the linked list.
            prev=x
            x=nxt

        return ans
