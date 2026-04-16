class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        """
        The stack is an array of tuples where the first element
        the value and the second element is the minimum of the
        stack.
        """
        # Check if the stack is empty
        if not self.stack:
            self.stack.append((val, val))
        else:
            previous_min = self.stack[-1][1]
            new_min = min(previous_min, val)
            self.stack.append((val, new_min))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
