class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def addBinary(self, A, B):
        result = ""
        carry = 0
        i ,j = len(A ) -1 ,len(B ) -1

        while i>= 0 or j >= 0:
            summ = carry
            if i >= 0:
                summ += ord(A[i]) - ord('0')
            if j >= 0:
                summ += ord(B[j]) - ord('0')
            i -= 1
            j -= 1

            carry = 1 if summ > 1 else 0
            result += str(summ % 2)
        if carry != 0:
            result += str(carry)
        return result[::-1]

'''class Solution:
	# @param A : string
	# @param B : string
	# @return a strings

    def addBinary(self, A, B):
        def get(x):
            if x == 0:
                return "0"
            if x == 1:
                return "1"

        n = -len(A)
        m = -len(B)
        nm = min(n, m)
        carry = 0
        ans = ""
        # we add bits from the rightmost bit to the leftmost bit
        for i in range(-1, nm - 1, -1):
            if i >= n and i >= m:
                v = ord(A[i]) + ord(B[i]) - 2 * ord('0') + carry
                carry = v // 2
                v -= 2 * carry
                ans += get(v)
            elif i >= n:
                v = ord(A[i]) - ord('0') + carry
                carry = v // 2
                v -= 2 * carry
                ans += get(v)
            else:
                v = ord(B[i]) - ord('0') + carry
                carry = v // 2
                v -= 2 * carry
                ans += get(v)
        if carry == 1:
            ans += get(carry)
        return ans[::-1]

    def addBinary(self, A, B):
        val = int(A,2) + int(B,2)
        return bin(val)[2:]'''
