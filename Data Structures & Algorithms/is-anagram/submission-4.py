class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts_1 = {}
        counts_2 = {}
        
        for letter in s:
            counts_1[letter] = counts_1.get(letter, 0) + 1
        
        for letter in t:
            counts_2[letter] = counts_2.get(letter, 0) + 1
        
        if counts_1 == counts_2:
            return True
        
        return False
