class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        if not matrix: 
            return False 
        

        l= 0 
        r= rows
        min_diff = float('inf')

        row = 0

        while l<r: 
            mid = l+ ((r-l)//2)

            element = matrix[mid][0]

            if target == element:
                return True 
            elif element > target: 
                r-=1
            else:
                if (target-element)<min_diff: 
                    row = mid
                    min_diff = (target-element)
                l+=1
        
        #return row

        l=0
        r=cols

        while (l<r):
            mid = l+ ((r-l)//2)
            element = matrix[row][mid]

            if target == element:
                return True 
            elif element > target: 
                r-=1
            else:
                l+=1
        
        return False



        