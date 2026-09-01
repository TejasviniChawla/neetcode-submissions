class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:

        nums = sorted(nums)
        print(nums)

        score= float('inf')

        for i in range(0, len(nums)-k+1):
            if (nums[k-1+i] - nums[i])< score: 
                score = nums[k-1+i] - nums[i]
            print(i, k-1, nums[k-1+i], nums[i], score)
        
        return score


        


        