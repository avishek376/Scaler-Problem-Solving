# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def reversell(self, head):
        prev = head

        cur = head.next
        cn = None

        prev.next = None

        while cur:
            cn = cur.next
            cur.next = prev
            prev = cur
            cur = cn
        return prev

        def reorderList(self, A):
            head = A

        if not head or not head.next:
            return head

        if not head.next.next:
            return head

        slow = fast = head
        prev = None

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        h2 = slow.next

        slow.next = None

        h2 = self.reversell(h2)

        # start merging

        cur1 = head
        cur2 = h2
        while cur1 and cur2:
            next1 = cur1.next
            next2 = cur2.next

            cur1.next = cur2
            cur2.next = next1

            cur1 = next1
            cur2 = next2
        return head
