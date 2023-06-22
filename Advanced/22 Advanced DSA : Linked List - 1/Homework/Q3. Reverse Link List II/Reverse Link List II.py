# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @param C : integer
    # @return the head node in the linked list
    def reverseBetween(self, A, B, C):
        head = A
        if head == None or head.next == None:
            return head
        dummy = ListNode(0)
        dummy.next = head
        head1 = dummy
        for i in range(B - 1):
            head1 = head1.next
        p = head1.next
        for i in range(C - B):
            tmp = head1.next
            head1.next = p.next
            p.next = p.next.next
            head1.next.next = tmp
        return dummy.next





'''# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def reverse(node):
    bef = None
    aft = None
    while node:
        aft = node.next
        node.next = bef
        bef = node
        node = aft

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @param C : integer
    # @return the head node in the linked list
    def reverseBetween(self, A, B, C):
        current = A
        first = None
        fromx = None
        to = None
        last = None
        count = 0
        while current!= None:
            count += 1
            if count < B:
                first = current
            if count == B:
                fromx = current
            if count == C:
                to = current
                last = to.next
                break
            current = current.next
        to.next = None
        reverse(fromx)
        if first != None:
            first.next = to
        else:
            A = to
        fromx.next = last
        return A'''