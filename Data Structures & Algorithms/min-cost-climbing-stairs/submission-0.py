class Solution:

    def minCostClimbingStairs(self, cost: List[int]) -> int:

        """
        @desc given cost array, find min cost of reaching top (last step+1) of the staircase - provided we can step either i+1, or i+2, starting from i -> -1 
        @args
            @arg1 cost -> list of int

        @return minumum cost of climb 

        dp(n) returns minimum cost of reaching n steps
        """

        """

        def dp(n):
            if n == 0: 
                return cost[0]
            if n == 1: 
                return cost[1]
            if n < 0: 
                return float("inf")
            
            return min(dp(n-1), dp(n-2)) + cost[n]
        
        return min(dp(len(cost)-1), dp(len(cost)-2))
        # dp(2) _. dp(1), dp0 + cost pn


        """

        prev1 = cost[1]
        prev2 = cost[0]

        for i in range(2, len(cost)): 
            current = min(prev1, prev2) + cost[i]
            prev2= prev1
            prev1= current 
        return min(prev1, prev2)
            



        