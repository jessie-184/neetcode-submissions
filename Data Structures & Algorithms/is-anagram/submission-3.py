class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Approach 1: Sorting
        # Time complexity O(n logn + m log m) | Space complexity O(n + m)
        # sorted() create new list because string is immutable 
        # return sorted(s) == sorted(t)

        # Approach 2: Dictionary counting characters
        # Time complexity O(n + m) | Space complexity O(1)
        # Space is constant because there are at most 26 characters 
        if len(s) != len(t):
            return False
        dictS, dictT = {}, {} 
        for i in range(len(s)):
            dictS[s[i]] = 1 + dictS.get(s[i], 0)
            dictT[t[i]] = 1 + dictT.get(t[i], 0)
        return dictS == dictT