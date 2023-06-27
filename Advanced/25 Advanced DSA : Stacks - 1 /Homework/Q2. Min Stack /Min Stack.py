class MinStack:

    # @param x, an integer
    # @return nothing
    def push(self, x):
        if len(self.stk) == 0:
            self.stk.append(x)
            self.mnstk.append(x)

        else:
            self.stk.append(x)
            if x <= self.mnstk[-1]:
                self.mnstk.append(x)

    # @return nothing
    def pop(self):
        if len(self.stk) > 0:
            val = self.stk.pop()
            if val == self.mnstk[-1]:
                self.mnstk.pop()
        else:
            return

    # @return an integer
    def top(self):
        if len(self.stk) > 0:
            return self.stk[-1]
        else:
            return -1

    # @return an integer
    def getMin(self):
        if len(self.mnstk) > 0:
            return self.mnstk[-1]
        else:
            return -1

    def __init__(self):
        self.stk = []
        self.mnstk = []