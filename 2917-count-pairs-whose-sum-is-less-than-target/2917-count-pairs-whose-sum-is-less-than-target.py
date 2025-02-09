class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort() # sort the vector nums
        count = 0 # variable to store the count
        left = 0 # variable to store the left
        right = len(nums)-1 # variable to store the right
        while(left < right): # loop until left is less than right
            if(nums[left] + nums[right] < target): # if nums[left] + nums[right] is less than target
                count += right-left # update the count
                left += 1 # increment the left
            else: # else
                right -= 1 # decrement the right
        return count # return the count

# class Solution:
#     def countPairs(self, nums: List[int], target: int) -> int:
#         ans = 0
#         s = 0
#         f = 0
#         while s != len(nums)-1:
#             if nums[s] + nums[f] < target:
#                 ans += 1
#             if nums[s] + nums[f] >= target:
#                 f = s+1
#                 s += 1
#             else:
#                 if f < len(nums)-1:
#                     f += 1
#                 else:
#                     f = s+1
#                     s += 1
#         return ans