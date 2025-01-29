class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        return sum(n if n < 10 else -n for n in nums) != 0