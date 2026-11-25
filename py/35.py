class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        i = 0
        while i < len(nums):
            n = nums[i]

            if n == target:
                return i
            
            if n > target:
                return i
            
            i += 1
        
        return i

print(Solution().searchInsert([1,3,5,6], 7)) # :) :)