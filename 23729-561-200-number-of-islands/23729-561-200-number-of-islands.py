class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def helper(i,j, grid):
            if i > len(grid) - 1 or j > len(grid[i]) - 1 or i < 0 or j < 0:
                return
            if grid[i][j] == "1":
                grid[i][j] = "0"
                helper(i+1, j, grid)
                helper(i-1, j, grid)
                helper(i, j+1, grid)
                helper(i, j-1, grid)
        
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    count += 1
                    grid[i][j] = "0"
                    helper(i+1, j, grid)
                    helper(i-1, j, grid)
                    helper(i, j+1, grid)
                    helper(i, j-1, grid)
        return count

        #time complx = O(M * N)
        #Space = O(M*N)