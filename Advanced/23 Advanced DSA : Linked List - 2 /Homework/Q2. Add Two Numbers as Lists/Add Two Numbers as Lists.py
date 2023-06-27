# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def addTwoNumbers(self, A, B):
        prev = None
        first = None
        carry, sum = 0, 0
        while (A != None or B != None or carry != 0):
            node = ListNode(0)
            # finds the value of each node
            sum = carry
            if (first == None):
                first = node
            if (prev != None):
                prev.next = node
            if (A != None):
                sum += A.val
                A = A.next
            if (B != None):
                sum += B.val
                B = B.next
            node.val = sum % 10
            sum //= 10
            carry = sum
            prev = node
        return first


'''
# Definition for singly-linked list.
# class ListNode:
#  def init(self, x):
#     self.val = x
#     self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def get_length(self, head):
        cur = head
        length = 0

        while cur:
            length += 1
            cur = cur.next

        return length

    def addTwoNumbers(self, A, B):
        a = self.get_length(A)
        b = self.get_length(B)

        if a < b: return self.addTwoNumbers(B, A)

        carry = 0
        cur = A
        pre = None

        while cur:
            summ = carry + cur.val + B.val if B else cur.val + carry

            cur.val = summ % 10
            carry = summ // 10

            pre = cur
            cur = cur.next
            if B: B = B.next

        while carry:
            val = carry % 10
            last = ListNode(val)

            pre.next = last
            pre = last

            carry //= 10

        return A
'''