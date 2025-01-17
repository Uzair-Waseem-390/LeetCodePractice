class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        nums2 = nums[len(nums)//2:]
        c = 0
        l = len(nums)
        for i in range(1, l, 2):
            nums.insert(i,nums2[c])
            c+=1
        return nums[:l]
