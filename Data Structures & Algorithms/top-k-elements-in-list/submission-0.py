class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Time Complexity O(n logn) | Space Complexity O(n)
        lookup = {}
        for num in nums:
            lookup[num] = 1 + lookup.get(num, 0)
        
        return sorted(lookup, key = lookup.get, reverse = True)[:k]