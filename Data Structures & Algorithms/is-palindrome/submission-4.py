class Solution:
    def isPalindrome(self, s: str) -> bool:

        s_lower = s.lower()
        s_final = ""

        for char in s_lower:
            if char.isalpha() or char.isnumeric():
                s_final += char
        
        left = 0
        right = len(s_final) - 1
        
        while left < right:

            if s_final[left] != s_final[right]:
                return False
            left += 1
            right -= 1
        
        
        return True
        
        