'''
For the purpose of this problem, define a palindromic string to be a string 
which when all the nonalphnumeric are removed it reads the same front to back 
ignoring case. For example, 
amanaplanacanalpanama, ablewasiereisawelba
'''

def is_palindrome(a_str):
    #parse the string
    palindrome = ""
    for i in range(len(a_str)):
        char = a_str[i]

        char = char.lower()
        if ord(char) >= ord('a') and ord(char) <= ord('z'):
            palindrome += char
    print(palindrome)
    def testPa(palindrome):
        left = 0
        right = len(palindrome)-1

        while(left <= right):
            if palindrome[left] != palindrome[right]:
                return False
            left+=1
            right-=1
        return True
    return testPa(palindrome)

print(is_palindrome("A man a plan, Canal!"))

    
