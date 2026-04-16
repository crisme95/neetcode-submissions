class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])
        
        stack = []

        for t in tokens:
            if t not in "+-*/":
                # Convert token to int before pushing to stack
                stack.append(int(t))
                continue
            result = 0
            if t == '+':
                right = stack.pop()
                left = stack.pop()
                result = left + right
            if t == '-':
                right = stack.pop()
                left = stack.pop()
                result = left - right
            if t == '*':
                right = stack.pop()
                left = stack.pop()
                result = left * right
            if t == '/':
                right = stack.pop()
                left = stack.pop()
                result = int(left / right)
            stack.append(result)
        
        return stack.pop()
            