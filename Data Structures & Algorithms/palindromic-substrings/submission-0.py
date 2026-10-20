class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        res = 0
        for i in range(n):
            x = 0
            while 0<=i-x<=i+x<n and s[i-x]==s[i+x]:
                res+=1
                x+=1
            x=0
            while 0<=i-x<=i+x+1<n and s[i-x]==s[i+x+1]:
                res+=1
                x+=1
            


        return res
                




        