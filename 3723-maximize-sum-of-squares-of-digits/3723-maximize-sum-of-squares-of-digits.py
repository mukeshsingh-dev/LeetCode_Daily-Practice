class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        # Maximum possible sum for `num` digits is 9 * num
        if sum > 9 * num or sum < 1:
            return ""
        
        # Calculate full 9s and remainder
        nines = sum // 9
        rem = sum % 9
        
        # Build the string greedily: 9s first, then remainder (if any), then trailing 0s
        if rem > 0:
            zeros = num - nines - 1
            return "9" * nines + str(rem) + "0" * zeros
        else:
            zeros = num - nines
            return "9" * nines + "0" * zeros