class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        hm = {}
        for i,v in enumerate(sentences):
                hm[i] = v.count(' ') + 1
        return max(hm.values())
                