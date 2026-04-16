class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if s is None:
            return 0
        
        if len(s) < 2:
            return 1
        
        left, max_f, res = 0, 0, 0
        chars = {}

        for right in range(len(s)):
            char = s[right]
            window = right - left + 1

            if char not in chars:
                chars[char] = 1
            else:
                chars[char] += 1

            if chars[char] > max_f:
                max_f = chars[char]
            
            if window - max_f > k:
                chars[s[left]] -= 1
                left += 1
                window -= 1
            
            res = window
        
        return res



        