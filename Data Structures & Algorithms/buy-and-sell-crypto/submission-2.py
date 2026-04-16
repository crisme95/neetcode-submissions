class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_buy, max_profit = None, 0

        for p in prices:
            if min_buy == None:
                min_buy = p
                continue
            
            if min_buy > p:
                min_buy = p
                print(min_buy)
            
            profit = p - min_buy

            if profit > max_profit:
                max_profit = profit

        return max_profit