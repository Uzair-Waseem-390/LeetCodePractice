class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        slow = 0
        for fast in range(len(needle), len(haystack)+1):
            if needle == haystack[slow:fast]:
                return fast - len(needle)
                break
            slow += 1
        return -1
                