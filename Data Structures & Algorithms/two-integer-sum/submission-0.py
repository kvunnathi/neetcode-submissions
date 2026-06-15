class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = {}

        for i, num in enumerate(nums):
            result[num] = i

        for i, num in enumerate(nums):
            diff = target - num
            if diff in result and result[diff] != i:
                return [i, result[diff]]
        return []