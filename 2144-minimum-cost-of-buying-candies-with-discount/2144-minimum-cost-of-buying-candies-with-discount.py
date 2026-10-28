from typing import List

class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        return sum(price for i, price in enumerate(cost) if i % 3 != 2)