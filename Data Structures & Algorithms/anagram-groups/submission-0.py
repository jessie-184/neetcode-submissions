class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Time complexity O(n) | Space complexity O(n)
        anagrams = {}
        sortedStr = ""
        for str in strs:
            sortedStr = "".join(sorted(str))
            if sortedStr not in anagrams:
                anagrams[sortedStr] = []
            anagrams[sortedStr].append(str)
        return list(anagrams.values())