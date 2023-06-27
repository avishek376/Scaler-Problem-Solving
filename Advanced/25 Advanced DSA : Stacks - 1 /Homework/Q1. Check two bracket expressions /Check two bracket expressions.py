class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def solve(self, A, B):
        def parse(string, n, global_sign, signs):
            # True stands for + and False for -
            for i in range(n):
                if string[i] == '+' or string[i] == '-':
                    continue
                if string[i] == '(':
                    if string[i-1] == '-':
                        global_sign.append(False == global_sign[-1])
                    else: # For + and (
                        global_sign.append(True == global_sign[-1])
                elif string[i] == ')':
                    global_sign.pop()
                else:
                    local_sign = True
                    if string[i-1] == '-':
                        local_sign = False
                    index = ord(string[i]) - ord('a')
                    signs[index] = local_sign == global_sign[-1]

        lenA, lenB = len(A), len(B)
        global_sign = [True]
        signs_for_a = [True] * 26
        signs_for_b = [True] * 26
        parse(A, lenA, global_sign, signs_for_a)
        parse(B, lenB, global_sign, signs_for_b)
        for i in range(26):
            if signs_for_a[i] != signs_for_b[i]:
                return 0
        return 1
