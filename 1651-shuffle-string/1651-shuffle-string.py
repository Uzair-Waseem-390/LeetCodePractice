class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        a = list(s)
        hm={}
        for i,v in enumerate(indices):
            hm[v] = a[i]
        hm = sorted(hm.items())
        s = ""
        for key, value in hm:
            s+=value
        return s

