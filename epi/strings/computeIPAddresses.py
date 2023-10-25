'''
A decimal string is a string consisting of digits between 0 and 9.
Internet Protocol (IP) addresses can be written as four decimal strings
separated by periods, e.g., 192.168.1.201. A careless programmer 
mangles a string representing an IP address in such a way that all the periods
vanish.

Write a program that determines where to add periods to a decimal string so that
the resulting string is a valid IP address. There may be more than one valid IP
address corresponding to a string, in whcih case you should print all possibilities
For example, if the mangled string is "19216811" then two corresponding IP add-
-resses are 192.168.1.1 and 19.216.81.1
'''

def compute(mangled):
    '''
    Internet protocol addresses can be written as four decimal strings separated by periods

    '''
    ans = []
    parts = []
    def is_valid_part(s):
        return len(s) == 1 or (s[0] != '0' and int(s) <= 255)
    
    def f(g):
        nonlocal ans
        if i >= len(mangled):
            if len(parts) == 4:
                temp = ""
                for p in parts:
                    temp += p + '.'
                ans.append(temp)
                parts = []
            return
    





