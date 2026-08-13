class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Time complexity O(n logn) | Space complexity O(n)
        # sorted() create new list because string is immutable 
        return sorted(s) == sorted(t)