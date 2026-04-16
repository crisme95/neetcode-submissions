import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if not piles or not h:
            return 0

        num_piles = len(piles)
        
        """
        Find the maximum eating rate by finding the largest pile
        """
        # k_max = 0
        # for pile in piles:
        #     if pile > k_max:
        #         k_max = pile

        k_max = max(piles)
        
        """
        Use binary search to find minimum k to eat all bananas
        """
        l, r, k_min = 1, k_max, k_max

        while l <= r:
            k = l + ((r - l) // 2)
            time = 0
            for p in piles:
                time += math.ceil(float(p) / k)

            if time <= h:
                k_min = k
                r = k - 1
            else:
                l = k + 1

        
        return k_min
