class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(char.lower() for char in s if char.isalnum())
        n = len(s)
        if n < 1:
            return True

        for i in range((n//2)+1):
            if s[i] != s[n-1-i]:
                return False
        return True

        