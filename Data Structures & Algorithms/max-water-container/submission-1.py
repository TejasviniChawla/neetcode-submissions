class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # [1,7,2,5,4,7,3,6]
        # waterHeld= min(heights[start_index],[end_index])*(end_index-start_index)

        #bruteforce: 

        """
        max_water = 0
        for i 0->n-1: 
            for j i+1, n: 
                max_water = max(max_water,min(heights[i],[j])*(j-i) )
        return max_water
        """
        max_water = 0
        n =len(heights)
        l, r= 0, n-1

        while l<r: 
            cur_area = min(heights[l],heights[r])*(r-l)
            if heights[l]< heights[r]: 
                l+=1
            else: 
                r-=1
            max_water = max(max_water, cur_area)
        return max_water
        