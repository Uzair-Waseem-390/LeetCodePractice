class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)
        for i in range(0,len(s),k*2):
            s[i:i + k] = reversed(s[i:i + k])
        return ''.join(s)
        
        
        # s = list(s)
        # l = len(s)
        # a = 0
        # for b in range(1,len(s),k*2):
        #     if k < l:
        #         s[a],s[b] = s[b],s[a]
        #         l -= k*2
        #         a += k*2
        #     else:
        #         break
        # return ''.join(s)