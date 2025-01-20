class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for i in s:
            if stack and stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)
        return "".join(stack)
        
        
        
        
        
        # s = list(s)
        # i = 0
        # while i < len(s) - 1:
        #     if s[i] == s[i + 1]:
        #         s.pop(i)
        #         s.pop(i)
        #         if i > 0:
        #             i -= 1
        #     else:
        #         i += 1
        # return ''.join(s)