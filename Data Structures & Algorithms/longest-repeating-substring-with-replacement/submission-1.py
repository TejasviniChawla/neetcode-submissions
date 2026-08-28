from collections import Counter 
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l =0
        ans = 0
        count = Counter()
        
        for r in range(len(s)):
            count[s[r]]+=1
            while (r-l-max(count.values())+1>k):
                count[s[l]]-=1
                l+=1

            ans = max(ans, r-l+1)
        return ans



        