from typing import List

class Solution:
    MOD = 10**9 + 7

    def numOfWays(self, nums: List[int]) -> int:
        n = len(nums)

        # Precompute combinations C[n][k] modulo MOD
        comb = [[0] * (n + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            comb[i][0] = 1
            comb[i][i] = 1

            for j in range(1, i):
                comb[i][j] = (
                    comb[i - 1][j - 1] +
                    comb[i - 1][j]
                ) % self.MOD

        def solve(arr: List[int]) -> int:
            if len(arr) <= 2:
                return 1

            root = arr[0]

            left = [x for x in arr[1:] if x < root]
            right = [x for x in arr[1:] if x > root]

            left_ways = solve(left)
            right_ways = solve(right)

            ways_to_merge = comb[len(left) + len(right)][len(left)]

            return (
                ways_to_merge
                * left_ways
                * right_ways
            ) % self.MOD

        # Subtract 1 to exclude the original ordering
        return (solve(nums) - 1) % self.MOD