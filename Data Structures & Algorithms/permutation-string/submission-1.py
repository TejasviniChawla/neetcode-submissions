from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = Counter(s1)
        l= len(s1)
        for r in range(0,len(s2)):
            
            cmp = Counter(s2[r:r+l])
            #print(cmp)
            if count==cmp:
                return True
            
        return False

        