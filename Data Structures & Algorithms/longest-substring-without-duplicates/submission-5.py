class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if (len(s)) < 1:
            return 0

        max_sub_s, sub_s, left = 0, set(), 0

        for right in range(len(s)):
            
            while s[right] in sub_s:
                sub_s.remove(s[left])
                left += 1
                
            sub_s.add(s[right])

            max_sub_s = max(len(sub_s), max_sub_s)
        
        return max_sub_s