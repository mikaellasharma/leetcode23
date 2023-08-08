# 5. Longest Palindromic Substring

class Solution:

    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        palindrome = ''
        palindrome_length = 0
        for i in range(length):
            j = i+1
            while j <= length:
                if self.isPalindrome(s[i:j]) and palindrome_length < len(s[i:j]):
                    palindrome = s[i:j]
                    palindrome_length = len(s[i:j])
                    if palindrome_length == length:
                        return palindrome
                j += 1
        return palindrome
    
    def isPalindrome(self, s):
        return s == s[::-1]
