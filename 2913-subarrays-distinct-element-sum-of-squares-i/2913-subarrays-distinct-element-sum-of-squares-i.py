from typing import List


class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        answer = 0
        n = len(nums)

        for left in range(n):
            distinct = set()

            for right in range(left, n):
                distinct.add(nums[right])
                count = len(distinct)
                answer += count * count

        return answer