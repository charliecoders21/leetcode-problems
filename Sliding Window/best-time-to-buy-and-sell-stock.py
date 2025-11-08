from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buying_price=prices[0]
        profit=0
        for item in range(len(prices)):
            if buying_price>prices[item]:
                buying_price=prices[item]
            profit=max(profit,prices[item]-buying_price)
        return profit