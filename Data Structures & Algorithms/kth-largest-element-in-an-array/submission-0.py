import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums or k < 1 or k is None:
            return None

        self.nums = nums
        self.k = k

        heapq.heapify(self.nums)

        while len(self.nums) != self.k:
            heapq.heappop(self.nums)

        return self.nums[0]

        