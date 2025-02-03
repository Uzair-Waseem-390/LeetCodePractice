class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for n in range(k):
            v = min(nums)
            i = nums.index(v)
            nums[i] = v * multiplier
        return nums  