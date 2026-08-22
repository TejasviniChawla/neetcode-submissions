class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        al = {}

        for string in strs: 
            alpha = [0]*26
            for c in string: 
                alpha[ord(c) - ord('a')]+=1
            alpha = tuple(alpha)

            al.setdefault(alpha, []).append(string)
        
        ans = []
        for v in al.values():
            ans.append(v)
        return ans
        
            