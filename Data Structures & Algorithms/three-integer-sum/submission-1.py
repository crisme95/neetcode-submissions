class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return [[]]
        
        nums = sorted(nums)
        triplets = set()

        for i in range(len(nums)):
            j, k = i + 1, len(nums) - 1
            target = -(nums[i])

            while j < k:
                if nums[j] + nums[k] < target:
                    j += 1
                elif nums[j] + nums[k] > target:
                    k -= 1
                else:
                    triplets.add(tuple([nums[i], nums[j], nums[k]]))
                    j += 1
                    k -= 1

        return [list(triplet) for triplet in triplets]
