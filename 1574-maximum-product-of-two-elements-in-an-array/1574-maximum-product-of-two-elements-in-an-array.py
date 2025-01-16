class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        v1 = max(nums)
        nums.pop(nums.index(v1))
        v2 = max(nums)
        nums.pop(nums.index(v2))
        return (v1 -1) * (v2 - 1)