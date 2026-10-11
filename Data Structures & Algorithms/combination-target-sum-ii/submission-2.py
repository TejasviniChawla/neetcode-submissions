class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = set()
        candidates.sort()

        def dfs(start_idx, remaining_target, current_comb):
            #print(start_idx, remaining_target, current_comb)

            if 0==remaining_target:
                result.add(tuple(current_comb))
                return
            
            for i in range(start_idx, len(candidates)):
                if candidates[i]>remaining_target:
                    break
                if i > start_idx and candidates[i] == candidates[i - 1]:
                    continue
                
                current_comb.append(candidates[i])
                dfs(i+1, remaining_target-candidates[i], current_comb)
                current_comb.pop()
            
        dfs(0, target, [])
        return [list(comb) for comb in result]




        