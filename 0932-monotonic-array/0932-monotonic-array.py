class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if nums == sorted(nums):
            return True
        elif nums == sorted(nums, reverse=True):
            return True
        else:
            return False
        
        # for i,v in enumerate(nums):
        #     if i < 