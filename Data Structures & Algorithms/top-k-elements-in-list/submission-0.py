class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in nums: 
            if i in d: 
                d[i]+=1
            else:
                d[i]=1
        
        sorted_d =sorted(d.items(), key = lambda x:x[1], reverse=True)
        ans = []
        
        for i in range(k):
            ans.append(sorted_d[i][0])
        return ans
            

       
