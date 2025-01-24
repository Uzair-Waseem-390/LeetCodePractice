class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if stack and i == ")":
                if stack[-1] == "(":
                    stack.pop()
                else:
                    return False
            elif stack and i == "}":
                if stack[-1] == "{":
                    stack.pop()
                else:
                    return False 
            elif stack and i == "]":
                if stack[-1] == "[":
                    stack.pop()
                else:
                    return False               
            else:
                stack.append(i)
        if len(stack) == 0:
            return True
        else:
            return False