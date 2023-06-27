'''
Definition for singly-linked list
class ListNode:
   def __init__(self, val):
      self.val = val
      self.next = None
'''
class Solution:
    def getIntersectionNode(self, A, B):
        list1 = A
        list2 = B

        list1_len = 0
        list2_len = 0

        cur = list1
        while cur:
            list1_len += 1
            cur = cur.next

        cur = list2
        while cur:
            list2_len += 1
            cur = cur.next

        bigger_list, smaller_list = (A, B) if list1_len > list2_len else (B, A)

        len_diff = abs(list1_len-list2_len)

        # Advance bigger list by difference
        while len_diff > 0:
            len_diff -= 1
            bigger_list = bigger_list.next

        # Both the lists are at same level when advanced and checked, should meet
        # if they are connected
        while bigger_list and smaller_list:
            if bigger_list == smaller_list:
                return bigger_list
            bigger_list = bigger_list.next
            smaller_list = smaller_list.next

        return None

'''
'''
# Definition for singly-linked list
# class ListNode:
#    def __init__(self, val):
#       self.val = val
#       self.next = None
'''
class Solution:
    def getIntersectionNode(self, A, B):
        hs = set()

        t = A;
        while t != None:
            hs.add(t)
            t = t.next;
       
        t = B;
        while t != None:
            if t in hs:
                return t;
            t = t.next;
       
        return None;
        
'''