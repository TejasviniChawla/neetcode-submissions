class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        n = len(nums)

        cur_sum = 0


        for i in range(n):
            cur_sum = max(0, cur_sum)+ nums[i]
            max_sum = max(max_sum, cur_sum)
            

        return max_sum
        