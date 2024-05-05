from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_day, sell_day = 0, 1
        max_profit = 0
        
        while sell_day < len(prices):
            if prices[buy_day] < prices[sell_day]:
                profit = prices[sell_day] - prices[buy_day]
                max_profit = max(max_profit, profit)
            else:
                buy_day = sell_day
            sell_day += 1

        return max_profit
        

case1_input = [7,1,5,3,6,4] 
case2_input = [7,6,4,3,1]

print(Solution().maxProfit(case1_input))
print(Solution().maxProfit(case2_input))