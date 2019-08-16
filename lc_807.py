class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        colMax = []
        cols = list(map(list, zip(*grid)))
        rowMax = []
        
        for i in grid:
            rowMax.append(max(i))
        
        for i in cols:
            colMax.append(max(i))
        
        eachMax = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                eachMax += min(rowMax[i], colMax[j]) - grid[i][j]
        
        return eachMax
        
