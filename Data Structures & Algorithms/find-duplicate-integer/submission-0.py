class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        if not nums:
            return None
        
        unique = set()

        for n in nums:
            if n in unique:
                return n
            else:
                unique.add(n)
        