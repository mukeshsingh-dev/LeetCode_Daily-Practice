from typing import List

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        squares = sorted((x * x for x in nums), reverse=True)

        positive_slots = (len(nums) + 1) // 2

        return (
            sum(squares[:positive_slots])
            - sum(squares[positive_slots:])
        )