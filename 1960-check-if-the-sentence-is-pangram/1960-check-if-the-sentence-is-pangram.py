class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        abc = set("abcdefghijklmnopqrstuvwxyz")
        sentence = set(sentence)
        return abc.issubset(sentence)
        