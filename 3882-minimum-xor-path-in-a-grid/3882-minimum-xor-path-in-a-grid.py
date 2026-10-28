from typing import List

class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        dp = [set() for _ in range(n)]
        dp[0] = {0}

        for row in grid:
            for j, value in enumerate(row):
                possible = dp[j]

                if j > 0:
                    possible = possible | dp[j - 1]

                dp[j] = {x ^ value for x in possible}

        return min(dp[-1])