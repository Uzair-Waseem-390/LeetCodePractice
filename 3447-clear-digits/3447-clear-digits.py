class Solution:
    def clearDigits(self, s: str) -> str:
        if s.isalpha():
            return s
        u = list(s)
        i = 0
        while i < len(u):
            if u[i].isdigit(): 
                if i > 0:  
                    u.pop(i - 1)
                    i -= 1  
                u.pop(i)  
            else:
                i += 1
        return ''.join(u)