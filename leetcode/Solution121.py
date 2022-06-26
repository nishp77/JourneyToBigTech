from typing import List
import sys

class Solution121:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = sys.maxsize
        profit = 0

        for i in range(len(prices)):
            if prices[i] < minPrice:
                minPrice = prices[i]

            elif prices[i] - minPrice > profit:
                profit = prices[i] - minPrice
        
        return profit