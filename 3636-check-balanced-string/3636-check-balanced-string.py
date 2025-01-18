class Solution:
    def isBalanced(self, num: str) -> bool:
        s = list(num)
        es = 0
        os = 0
        for i in range(0, len(s), 2):
            es += int(s[i])
        for i in range(1, len(s), 2):
            os += int(s[i])
        print(es, os)
        if es == os:
            return True
        return False