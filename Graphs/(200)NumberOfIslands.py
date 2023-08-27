class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(grid, row, column):
            if row < 0 or row == len(grid) or column < 0 or column == len(grid[row]) or grid[row][column] == "0":
                return

            grid[row][column] = "0"
            dfs(grid, row + 1, column)
            dfs(grid, row - 1, column)
            dfs(grid, row, column + 1)
            dfs(grid, row, column - 1)

        answer = 0

        for rowIndex, row in enumerate(grid):
            for columnIndex, column in enumerate(row):
                if column == "1":
                    dfs(grid, rowIndex, columnIndex)
                    answer += 1

        return answer