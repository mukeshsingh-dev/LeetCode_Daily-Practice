class Solution:

    def closedIsland(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def dfs(r: int, c: int):
            # If out of bounds or water, stop
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 1:
                return

            # Mark current cell as visited/water
            grid[r][c] = 1

            # Traverse 4-directionally
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # Step 1: Remove all islands connected to the boundary
        for r in range(rows):
            for c in range(cols):
                # Check if cell is on the border and is land (0)
                if (
                    r == 0 or r == rows - 1 or c == 0 or c == cols - 1
                ) and grid[r][c] == 0:
                    dfs(r, c)

        # Step 2: Count the remaining closed islands
        closed_islands_count = 0
        for r in range(1, rows - 1):
            for c in range(1, cols - 1):
                if grid[r][c] == 0:
                    closed_islands_count += 1
                    dfs(r, c)  # Mark the whole island as visited

        return closed_islands_count