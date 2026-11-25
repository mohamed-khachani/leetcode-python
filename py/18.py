class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        res = []
        hashes = set()

        for i in range(len(nums) - 3):
            a = nums[i]

            for j in range(i+1, len(nums) - 2):
                b = nums[j]

                z = j + 1
                k = len(nums) - 1

                while z < k:
                    c = nums[z]
                    d = nums[k]
                    total = a + b + c + d


                    if total < target:
                        z += 1

                    elif total > target:
                        k -= 1

                    else:
                        if i != j and j != z and z != k:
                            hash = f'{a},{b},{c},{d}'
                            if hash not in hashes:
                                res.append([a, b, c, d])
                                hashes.add(hash)

                        z += 1
                        k -= 1

                        while z < k and nums[z] == nums[z - 1]:
                            z += 1

        return res

print(Solution().fourSum([2,2,2,2,2], 8)) #