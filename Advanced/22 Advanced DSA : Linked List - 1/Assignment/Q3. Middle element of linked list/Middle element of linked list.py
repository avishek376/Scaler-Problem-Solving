# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return an integer

    def solve(self, A):
        slow = fast = A
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

        return slow.val


'''
# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    def findlength(self,head):
        count = 0
        
        temp = head 
        while temp:
            temp = temp.next
            count += 1
            
        return count

    def solve(self, A):
        if not A or not A.next:
            return A
        
        N = self.findlength(A)
        
        to_find = (N//2) 
        
        temp = A
        while to_find != 0:
            temp = temp.next
            to_find -= 1
            
        return temp.val'''