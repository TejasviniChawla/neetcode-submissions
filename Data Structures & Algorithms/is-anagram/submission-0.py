class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d_s = {}
        d_t = {}
        for i in s: 
            if i in d_s: 
                d_s[i]+=1
            else: 
                d_s[i]= 0
        for i in t: 
            if i in d_t: 
                d_t[i]+=1
            else: 
                d_t[i]= 0 
        
        return d_s==d_t