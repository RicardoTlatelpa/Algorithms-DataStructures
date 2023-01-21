#include<iostream>
/*
Binary Strings
Count the number of binary strings with no consecutive ones that can be formed
using a binary string of Length N

Input
N
Output
Count of strings

Base cases:
length 1 
[1,0] count = 2
length 2
[10,01,00] count = 3
length 3
[000,100,010,001,101]

n <= 2 return n + 1

How do previous lengths help find the answer to the nth case?
f(n-1) + f(n-2)

*/