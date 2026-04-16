class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]

        l, r = 0, len(nums) - 1
        min_num = nums[0]

        while l <= r:
            m = l + ((r - l) // 2)
            print(f"l: {l}, m: {m}, r: {r}\n")
            if nums[l] < nums[m]:
                l = m
                if nums[l] < min_num:
                    min_num = nums[l]
            elif nums[m] < nums[r]:
                r = m
                if nums[r] < min_num:
                    min_num = nums[r]
            else:
                return min(min_num, nums[l], nums[r])