"""
https://leetcode.com/problems/valid-palindrome/description/

Check if a string is a palindrome or not.
Parse --> then test palindrome
"""

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s.replace("", " ")
        i = 0
        a = "abcdefghijklmnopqrstuvwxyz"

        alpha = [b for b in a]        
        test_string = []
        for c in range(len(s)):
            if s[c].lower() in alpha or s[c].isnumeric() :                
                test_string.append(s[c])
        j = len(test_string) -1
        
        s = test_string
        print(s)
        while(i < j):
            if(s[i].lower() != s[j].lower()):
                return False
            i += 1
            j -= 1
        return True