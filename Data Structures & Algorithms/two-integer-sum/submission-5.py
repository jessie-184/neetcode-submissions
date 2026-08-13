class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Approach 1: Nested loop
        # Time complexity O(n^2) | Space complexity O(1)
        # first, second = -1, -1
        # for i in range(len(nums)):
        #     j = i + 1
        #     while j < len(nums):
        #         sum = nums[i] + nums[j]
        #         if sum == target:
        #             first, second = i, j
        #             break
        #         j = j + 1
        #     if first != -1:
        #         break
        # return [first, second]

        # Approach 2: Value-Index dictionary
        # Time complexity O(n) | Space complexity O(n)
        lookup = {}
        for i, num in enumerate(nums):
            if num not in lookup:
                lookup[num] = []
            lookup[num].append(i)
        
        for key in lookup:
            remain = target - key
            if remain == key and len(lookup[key]) > 1:
                return [lookup[key][0], lookup[key][1]]
            if remain != key and remain in lookup:
                return [lookup[key][0], lookup[remain][0]]
        return [-1, -1]
