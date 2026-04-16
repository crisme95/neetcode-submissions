class TimeMap:

    def __init__(self):
        # Key: string -> Value: List of [timestamp, value] tuples
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        # 1. If key doesn't exist, return empty string
        if key not in self.store:
            return ""
        
        values = self.store[key]
        l, r = 0, len(values) - 1
        res = ""

        # 2. Binary Search for the largest timestamp <= target
        while l <= r:
            m = l + ((r - l) // 2)
            if values[m][0] <= timestamp:
                # This is a potential candidate, but there might be a 
                # closer one to the right
                res = values[m][1]
                l = m + 1
            else:
                r = m - 1
        
        return res