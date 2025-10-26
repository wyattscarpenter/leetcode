class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        row_count = len(grid)
        col_count = len(grid[0])
        def eat(row, col) -> None:
            if row < 0 or col < 0 or row > row_count-1 or col > col_count-1:
                return
            elif grid[row][col] == "0":
                return
            else:
                grid[row][col] = "0"
                eat(row+1, col)
                eat(row, col+1)
                eat(row-1, col)
                eat(row, col-1)
        count = 0
        for row in range(row_count):
            for col in range(col_count):
                if grid[row][col] == "1":
                    count+=1
                    eat(row, col)
        return count
