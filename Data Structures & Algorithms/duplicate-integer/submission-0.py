class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         dupe = False
         dupeSet = set(nums)

         if len(dupeSet) < len(nums):
            return True
         else:
            return False
            
