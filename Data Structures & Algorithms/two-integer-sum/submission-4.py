class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        for i in range(len(nums)): 
            complement = target-nums[i]
            if nums[i] in m:
                a= m[nums[i]][1]
                b= i
                return [a,b] if a<b else [b,a]
                
            else:
                m[complement] = (nums[i], i)
