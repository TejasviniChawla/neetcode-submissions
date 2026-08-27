class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # [10, 10, 1, 1, 1, 1]
        # [10, 1, 5, 6, 7, 1]
        l, r= 0, 1
        maxP = 0

        while r<len(prices):

            if prices[l]<prices[r]:
                maxP=max(maxP, prices[r]-prices[l])
            else: 
                l=r
            r+=1
        
        return maxP
            

        