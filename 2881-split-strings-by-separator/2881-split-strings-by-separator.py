class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        hm = []
        for word in words:
            parts = word.split(separator)
            hm.extend(part for part in parts if part)
        return hm
