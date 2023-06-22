class Solution:
	# @param A : head node of linked list
	# @param B : integer
	# @return the head node in the linked list
	def removeNthFromEnd(self, A, B):
            t1,t2 = A, A
            sz = 0
            # calculates the size of the linked list
            while (t1):
                t1 = t1.next
                sz += 1
            if B >= sz:
                A = A.next
            else:
                for i in range(sz - B - 1):
                    t2 = t2.next
                t2.next = t2.next.next
            return A


