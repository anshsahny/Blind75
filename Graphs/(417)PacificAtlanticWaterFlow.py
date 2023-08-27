class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def dfs(row, column, visited, prevHeight):
            if row < 0 or row == len(heights) or column < 0 or column == len(heights[row]) or (row, column) in visited or prevHeight > heights[row][column]:
                return

            visited.add((row, column))
            dfs(row + 1, column, visited, heights[row][column])
            dfs(row - 1, column, visited, heights[row][column])
            dfs(row, column + 1, visited, heights[row][column])
            dfs(row, column - 1, visited, heights[row][column])

        pacific, atlantic = set(), set()

        for i, row in enumerate(heights):
            dfs(i, 0, pacific, row[0])
            dfs(i, len(row) - 1, atlantic, row[-1])

        for j in range(len(heights[0])):
            dfs(0, j, pacific, heights[0][j])
            dfs(len(heights) - 1, j, atlantic, heights[-1][j])

        intersection = pacific & atlantic
        return list(intersection)