class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Time complexity O(n^2) | Space complexity O(1)
        first, second = -1, -1
        for i in range(len(nums)):
            j = i + 1
            while j < len(nums):
                sum = nums[i] + nums[j]
                if sum == target:
                    first, second = i, j
                    break
                j = j + 1
            if first != -1:
                break
        return [first, second]
