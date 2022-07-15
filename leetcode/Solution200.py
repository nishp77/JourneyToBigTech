from collections import deque
from typing import List


class Solution200:
    def numIslands(self, grid:List[List[str]]) -> int:
        if not grid: return 0

        rows, cols = len(grid), len(grid[0])
        visit = set()
        islands = 0

        def bfs(r,c):
            q = deque()
            q.append((r,c))
            visit.add((r,c))

            while q:
                row,col = q.popleft()
                directions = [[1,0],[-1,0],[0,1],[0,-1]]

                for dr,dc in directions:
                    r,c = row+dr, col+dc

                    if r in range(rows) and c in range(cols) and grid[r][c]=="1" and (r,c) not in visit:
                        visit.add((r,c))
                        q.append((r,c))
            


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visit:
                    bfs(r,c)
                    islands += 1
        
        return islands

        # if not grid: return 0
        
        # island = 0
        
        # def dfs(grid,i,j):
        #     if i<0 or i>= len(grid) or j<0 or j>= len(grid[0]) or grid[i][j] == "0":
        #         return 0
        #     grid[i][j] = "0"
        #     dfs(grid,i+1,j)
        #     dfs(grid,i-1,j)
        #     dfs(grid,i,j+1)
        #     dfs(grid,i,j-1)
        #     return 1
        
        # for r in range(len(grid)):
        #     for c in range(len(grid[0])):
        #         if grid[r][c] =="1":
        #             island += dfs(grid,r,c)
        
        # return island

            