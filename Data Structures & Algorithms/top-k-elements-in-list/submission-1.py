class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    
        # 1. Count frequencies of each number
        # {num: freq}
        # Example: {1: 2, 2: 3, 3: 1}
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        # 2. Build your map where *counts are the keys*
        # {freq: [list of nums]}
        freq_map = {}
        for num, freq in counts.items():
            if freq not in freq_map:
                freq_map[freq] = []
            freq_map[freq].append(num)
            
        # Example: {2: [1], 3: [2], 1: [3]}
        # 

        # 3. Get the keys (frequencies) and sort them, high-to-low
        sorted_freqs = sorted(freq_map.keys(), reverse=True)
        # Example: [3, 2, 1]

        # 4. Iterate from the back (highest freq) and add to result
        result = []
        for freq in sorted_freqs:
            # Add all numbers that had this frequency
            for num in freq_map[freq]:
                result.append(num)
                # If we've hit k, we're done
                if len(result) == k:
                    return result
                    
        return result