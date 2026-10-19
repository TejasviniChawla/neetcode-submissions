class Solution:
    def rob(self, nums: List[int]) -> int:
        """ 
        dp(n) -> max money we can make from n houses 

        base case: 
            - dp(0) -> nums[0]
            - dp(1) -> nums[1]
        
        recursive case: 
            - dp(n) -> max(dp(n-1), dp(n-2)+nums[n])

        """
        #approach 1
        """
        def dp(n): 
            if n==0: 
                return nums[0]
            if n==1: 
                return nums[1]
            return max(dp(n-1), dp(n-2)+nums[n])
        n = len(nums)
        return max(dp(n-1), dp(n-2))
        """

        #approach 2 
        if len(nums)==1: 
            return nums[0]

        prev1= max(nums[1], nums[0])
        prev2= nums[0]

        for i in range(2, len(nums)):
            current = max(prev1, prev2+nums[i])
            prev2 = prev1
            prev1 = current 

        return prev1


    

        