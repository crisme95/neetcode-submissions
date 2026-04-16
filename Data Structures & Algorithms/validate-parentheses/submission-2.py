class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        stack = []
        for p in s:
            if p in '({[':
                stack.append(p)
                continue
            if p in ']})':
                if stack:
                    opening_p = stack.pop()
                else:
                    opening_p = ''
                if opening_p == '(' and p == ')':
                    continue
                if opening_p == '{' and p == '}':
                    continue
                if opening_p == '[' and p == ']':
                    continue
                return False
        if stack:
            return False
        return True
