class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        if not nums:
            return None
        
        for i in range(len(nums)):
            index = abs(nums[i])
            num = nums[index]

            if num < 0:
                return index
            
            nums[index] *= -1