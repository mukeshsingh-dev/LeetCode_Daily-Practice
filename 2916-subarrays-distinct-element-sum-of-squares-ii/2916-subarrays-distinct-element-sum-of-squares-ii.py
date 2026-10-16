from typing import List

class Solution:
    MOD = 10**9 + 7

    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)

        total = [0] * (4 * n)   # sum of distinct counts
        square = [0] * (4 * n)  # sum of squared distinct counts
        lazy = [0] * (4 * n)

        def apply(node, left, right, value):
            length = right - left + 1

            square[node] = (
                square[node]
                + 2 * value * total[node]
                + length * value * value
            ) % self.MOD

            total[node] = (
                total[node] + length * value
            ) % self.MOD

            lazy[node] += value

        def push(node, left, right):
            if lazy[node] == 0 or left == right:
                return

            mid = (left + right) // 2
            value = lazy[node]

            apply(node * 2, left, mid, value)
            apply(node * 2 + 1, mid + 1, right, value)

            lazy[node] = 0

        def update(node, left, right, qleft, qright):
            if qleft > right or qright < left:
                return

            if qleft <= left and right <= qright:
                apply(node, left, right, 1)
                return

            push(node, left, right)

            mid = (left + right) // 2

            update(node * 2, left, mid, qleft, qright)
            update(node * 2 + 1, mid + 1, right, qleft, qright)

            total[node] = (
                total[node * 2] + total[node * 2 + 1]
            ) % self.MOD

            square[node] = (
                square[node * 2] + square[node * 2 + 1]
            ) % self.MOD

        last = {}
        answer = 0

        for right, value in enumerate(nums):
            previous = last.get(value, -1)

            # New value for subarrays starting at previous + 1 ... right
            update(1, 0, n - 1, previous + 1, right)

            answer = (answer + square[1]) % self.MOD
            last[value] = right

        return answer