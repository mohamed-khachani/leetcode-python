class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()

        closest = nums[0] + nums[1] + nums[2]

        for i in range(len(nums) - 2):
            a = nums[i]

            if i > 0 and a == nums[i - 1]:
                continue

            j = i + 1
            k = len(nums) - 1

            while j < k:
                total = a + nums[j] + nums[k]

                if abs(total - target) < abs(closest - target):
                    closest = total

                if total < target:
                    j += 1

                elif total > target:
                    k -= 1

                else:
                    return total

        return closest


print(Solution().threeSumClosest([-1, 2, 1, -4], 1))
        

print(Solution().threeSumClosest([-1,2,1,-4], 1))