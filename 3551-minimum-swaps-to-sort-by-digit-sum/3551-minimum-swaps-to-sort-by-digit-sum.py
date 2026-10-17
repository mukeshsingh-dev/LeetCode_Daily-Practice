from typing import List

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def digit_sum(x: int) -> int:
            total = 0
            while x:
                total += x % 10
                x //= 10
            return total

        n = len(nums)

        # Desired sorted order
        target = sorted(nums, key=lambda x: (digit_sum(x), x))

        # Map each value to its target index
        target_index = {
            value: i for i, value in enumerate(target)
        }

        visited = [False] * n
        swaps = 0

        for i in range(n):
            if visited[i] or target_index[nums[i]] == i:
                continue

            # Find cycle length
            cycle_length = 0
            current = i

            while not visited[current]:
                visited[current] = True
                current = target_index[nums[current]]
                cycle_length += 1

            # A cycle of length k requires k - 1 swaps
            swaps += cycle_length - 1

        return swaps