"""
https://leetcode.com/problems/valid-palindrome/description/

Check if a string is a palindrome or not.
Parse --> then test palindrome
"""

class Solution(object):
    def isalpha(self, char):
        return(("a" <= char <= "z") or ("0" <= char <= "9"))
    def isPalindrome(self, s):
        test_string = []
        for i in range(len(s)):
            if self.isalpha(s[i].lower()):
                test_string.append(s[i].lower())
        i = 0
        j = len(test_string) - 1
        while(i < j):
            if test_string[i] != test_string[j]:
                return False
            i += 1
            j -= 1
        return True

class Solution2(object):
    def isalpha(self, char):
        return(("a" <= char <= "z") or ("0" <= char <= "9"))
    def isPalindrome(self, s):
        l,r = 0, len(s) - 1
        while l < r:
            while l < r and not self.isalpha(s[l]):
                l+=1
            while r > l and not self.isalpha(s[r]):
                r-=1
            if s[l].lower() != s[r].lower():
                return False
            l,r = l + 1, r -1
        return True

my = Solution()
print((my.isPalindrome("d;';';';';';';',ad,,,,,")))