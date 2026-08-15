class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Approach 1: Hashmap frequency
        # Time Complexity O(n logn) | Space Complexity O(n)
        # lookup = {}
        # for num in nums:
        #     lookup[num] = 1 + lookup.get(num, 0)
        
        # return sorted(lookup, key = lookup.get, reverse = True)[:k]

        # Approach 2: Bucket Sort
        # Time Complexity O(n) | Space Complexity O(n)
        lookup = {}
        for num in nums:
            lookup[num] = 1 + lookup.get(num, 0)

        freq_bucket = [[] for i in range(len(nums) + 1)]
        for num, count in lookup.items():
            freq_bucket[count].append(num)

        result = []
        for i in range(len(nums), 0, -1):
            if len(freq_bucket[i]) == 0:
                continue
            else:
                for num in freq_bucket[i]:
                    result.append(num)
                    if len(result) == k:
                        return result



