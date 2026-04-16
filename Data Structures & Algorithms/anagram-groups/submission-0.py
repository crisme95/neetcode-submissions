class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        buckets = {}

        for s in strs:
            key = "".join(sorted(s))
            if key not in buckets:
                buckets[key] = []

            buckets[key].append(s)

        return list(buckets.values())

