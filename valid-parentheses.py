class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in ('(', '[', '{'):
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                else:
                    e = stack.pop()
                    if (c == ')' and e != '(') or (c == ']' and e != '[') or (c == '}' and e != '{'):
                        return False
        return len(stack) == 0
