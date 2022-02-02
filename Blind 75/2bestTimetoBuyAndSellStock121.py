class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lP = 0 #Buy
        rP = 1 #Sell
        maxP = 0       
        while rP < len(prices):
            if prices[lP] < prices[rP]:
                # Profit
                profit = prices[rP] - prices[lP]
                maxP = max(maxP, profit)
            else:
                lP = rP
            rP += 1   
        
        return maxP    