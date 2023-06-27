# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param A : head node of linked list
	# @return an integer
	def lPalin(self, A):
         head=A
         slow=head
         fast=head
         while fast!=None and fast.next!=None:
             fast=fast.next.next
             slow=slow.next
         # to reverse the given Linkedlist from mid to tail
         prev=None
         curr=slow
         while curr!=None:
             temp=curr.next
             curr.next=prev
             prev=curr
             curr=temp
         while prev!=None:
             if prev.val!=head.val:
                 return 0
             head=head.next
             prev=prev.next
         return 1
