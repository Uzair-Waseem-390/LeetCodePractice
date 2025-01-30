class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 0
        for fast in range(1, len(nums)):
            if nums[slow] != nums[fast]:
                slow += 1
                nums[slow] = nums[fast]
        return slow + 1
        
        
        # map = set(nums)
        # nums[:len(map)] = sorted(map)
        # del nums[len(map):]
        # return len(nums)