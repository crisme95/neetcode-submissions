class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        freq_t = {}

        for c in t:
            freq_t[c] = freq_t.get(c, 0) + 1
        
        count = len(t)
        min_length = len(s) + 1
        start = 0
        res = ""

        for i in range(len(s)):
            # Expand the window
            if s[i] in freq_t:
                freq_t[s[i]] -= 1
                if freq_t[s[i]] >= 0:
                    count -= 1
            
            # Shrink the window
            while count == 0:
                # We use (i - start + 1) for length
                if (i - start + 1) < min_length:
                    min_length = i - start + 1
                    res = s[start : i + 1]

                # Remove element from left
                if s[start] in freq_t:
                    freq_t[s[start]] += 1
                    if freq_t[s[start]] > 0:
                        count += 1
                start += 1

        return res