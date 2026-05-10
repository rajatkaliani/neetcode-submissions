class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ""
        for char in s:
            if char.isalnum():
                cleaned += (char)
        return cleaned.lower() == cleaned[::-1].lower()