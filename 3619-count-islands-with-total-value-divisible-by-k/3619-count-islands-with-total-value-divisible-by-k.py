class Solution:
    def countIslands(self, grid, k):
        rows = len(grid)
        cols = len(grid[0])
        result = 0

        directions = [
            (-1, 0), (1, 0),
            (0, -1), (0, 1)
        ]

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] <= 0:
                    continue

                stack = [(r, c)]
                total = grid[r][c]
                grid[r][c] = 0  # Mark as visited

                while stack:
                    current_r, current_c = stack.pop()

                    for dr, dc in directions:
                        nr = current_r + dr
                        nc = current_c + dc

                        if (
                            0 <= nr < rows and
                            0 <= nc < cols and
                            grid[nr][nc] > 0
                        ):
                            total += grid[nr][nc]
                            grid[nr][nc] = 0
                            stack.append((nr, nc))

                if total % k == 0:
                    result += 1

        return result