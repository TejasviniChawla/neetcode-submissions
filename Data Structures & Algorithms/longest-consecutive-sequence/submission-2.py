class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        seen = set()

        for i in nums: 
            seen.add(i)
        
        ans = 1


        for i in seen: 
            count = 1
            while (i+count in seen and i-1 not in seen): 
                count+=1 
            ans = max(count, ans)
        return ans       