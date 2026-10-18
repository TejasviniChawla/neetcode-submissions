class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        seen = set()
        maxArea = 0

        rows, cols = len(grid), len(grid[0])
        directions = [(0,1), (0, -1), (1, 0), (-1, 0)]


        def dfs(row, col, curArea): 
            seen.add((row, col))

            for x, y in directions: 
                if 0<=row+x<rows and 0<=col+y<cols and (row+x, col+y) not in seen and grid[row+x][col+y]==1: 
                    curArea = dfs(row+x, col+y, curArea+1)
            
            return curArea


        for row in range(rows): 
            for col in range(cols):
                if grid[row][col] == 1 and (row, col) not in seen:
                    maxArea = max(maxArea, dfs(row, col, 1))
                
        return maxArea

        