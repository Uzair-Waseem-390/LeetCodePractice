class Solution:
    def findGCD(self, nums: List[int]) -> int:
        l = max(nums)
        s = min(nums)
        while s:
            l, s = s, l % s
        return l