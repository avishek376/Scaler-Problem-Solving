class Solution:
	# @param A : string
	# @param B : string
	# @return a strings
    def addBinary(self, A, B):
        carry = summ = 0
        res = ""
        i = len(A) - 1
        j = len(B) - 1
        while i >= 0 or j >= 0:
            summ = carry
            if i >= 0:
                summ += int(A[i]) - 0
            if j >= 0:
                summ += int(B[j]) - 0
            res += str(summ % 2)
            carry = summ // 2
            i -= 1
            j -= 1
        if carry != 0:
            res += '1'
        return ("".join(reversed(res)))
