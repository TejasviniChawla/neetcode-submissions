class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(start_idx, remaining_target, current_combination):
            #print(start_idx, remaining_target, current_combination)
            if remaining_target==0: 
                result.append(current_combination.copy())
                return
        
            for i in range(start_idx, len(nums)):
                if nums[i]>remaining_target:
                    continue
                current_combination.append(nums[i])
                dfs(i, remaining_target - nums[i], current_combination)
                current_combination.pop()
            
        dfs(0, target, [])
        return result
               
                    
                


        