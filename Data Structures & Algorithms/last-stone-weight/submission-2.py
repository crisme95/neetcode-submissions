import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones:
            return 0
        
        self.stones = [-s for s in stones]
        heapq.heapify(self.stones)

        while len(self.stones) > 1:
            
            heaviestStone, secondHeaviestStone = -(heapq.heappop(self.stones)), -(heapq.heappop(self.stones))
            
            if heaviestStone > secondHeaviestStone:
                weight = heaviestStone - secondHeaviestStone
                heapq.heappush(self.stones, -weight)
        
        if self.stones:
            return -(self.stones[0])
        
        return 0


        