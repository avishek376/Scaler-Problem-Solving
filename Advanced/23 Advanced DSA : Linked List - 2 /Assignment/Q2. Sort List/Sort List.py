# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def mergeLL(self, list1, list2):

        if not list1: return list2
        if not list2: return list1
        if not list1 and list2: return None

        head = None
        if list1.val < list2.val:
            head = list1
            list1 = list1.next
        else:
            head = list2
            list2 = list2.next

        temp = head
        while list1 and list2:
            if list1.val < list2.val:
                temp.next = list1
                list1 = list1.next
            else:
                temp.next = list2
                list2 = list2.next

            temp = temp.next

        if list1:
            temp.next = list1
        else:
            temp.next = list2

        return head


    def getMid(self, head):
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None
        return mid

    def sortList(self, head):
        if not head or not head.next:
            return head

        mid = self.getMid(head)

        left = self.sortList(head)

        right = self.sortList(mid)

        return self.mergeLL(left, right)
