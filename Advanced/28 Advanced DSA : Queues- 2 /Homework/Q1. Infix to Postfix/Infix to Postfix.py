class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        operators = {'^': 3,
                     '/': 2,
                     '*': 2,
                     '+': 1,
                     '-': 1,
                     }
        res = ''
        stack = []

        for i in range(len(A)):
            cur = A[i]

            if cur.isalpha():
                res = res + A[i]


            elif cur in operators:
                if not stack:
                    stack.append(cur)
                else:
                    while stack and stack[-1] != '(' and operators.get(cur) <= operators.get(stack[-1]):
                        res = res + stack[-1]
                        stack.pop()
                    stack.append(cur)

            elif cur == '(' or cur == ')':
                if cur == ')':
                    while stack and stack[-1] != '(':
                        if stack[-1] in operators:
                            res = res + stack[-1]
                        stack.pop()
                    stack.pop()
                else:
                    stack.append(cur)

        while stack:
            res = res + stack.pop()

        return res
