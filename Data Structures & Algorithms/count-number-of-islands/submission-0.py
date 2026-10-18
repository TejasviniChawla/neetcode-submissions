class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        seen = set()
        numIslands = 0
        directions = [(0,1), (0, -1), (1,0), (-1, 0)]

        def dfs(row, col, seen):
            seen.add((row, col))
            for x,y in directions: 
                if 0<=row+x<rows and 0<=y+col<cols and (row+x,col+y) not in seen and grid[row+x][col+y]=='1': 
                    dfs(row+x,col+y, seen)
            


        for row in range(0,rows): 
            for col in range(0,cols): 
                if grid[row][col]=='1' and (row, col) not in seen: 
                    
                    dfs(row, col, seen)
                    numIslands+=1

        return numIslands


