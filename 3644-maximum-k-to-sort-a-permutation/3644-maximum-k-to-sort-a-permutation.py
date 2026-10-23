class Solution:
    def sortPermutation(self, nums: list[int]) -> int:
        answer = None

        for i, value in enumerate(nums):
            if value != i:
                answer = value if answer is None else answer & value

        return 0 if answer is None else answer