import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if not points or k < 1 or k is None:
            return [[]]

        self.points = points
        self.k = k

        self.res = []

        for p in points:
            distance = self.euclideanDistance(p[0], 0, p[1], 0)
            self.res.append((-distance, p))
            
        heapq.heapify(self.res)

        while len(self.res) > k:
            heapq.heappop(self.res)
        
        return [r[1] for r in self.res]
        

    def euclideanDistance(self, x1, x2, y1, y2) -> float:
        
        return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
        