class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s = list(s)
        hm = {}
        for i,v in enumerate(s):
            if not v.isalpha():
                hm[i] = v
        s = [x for x in s if x.isalpha()]
        s.reverse()
        for key, value in hm.items():
            s.insert(key, value)
        return ''.join(s)
