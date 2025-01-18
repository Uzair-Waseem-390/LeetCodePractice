class Solution:
    def finalString(self, s: str) -> str:
        hm = []
        for i in range(len(s)):
            hm.append(s[i])
            if s[i] == 'i':
                hm.pop(len(hm)-1)
                hm.reverse()
                i -= 1
        return ''.join(hm)