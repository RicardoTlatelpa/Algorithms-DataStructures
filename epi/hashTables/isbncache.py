'''
12.3 ISBN Cache

The international standard book number is a unique commercial book 
identifier. It is a string of length 10. The first 9 characters are digits,
the last character is a check character. The check character is the sum of the 
first 9 digits, mod 11, with 10 represented by 'X'. (Modern ISBNs use 13 digits),
and the check digit is taken mod 10; this problem is concerned with 10-digit ISBNs).

Create a cahce for looking up prices of books identified by their ISBN.
You implement a lookup, insert, and remove methods. Use the recently used
policy for cache eviction. If an ISBN is already present, insert should not change 
the price, but it should update that entry to be the most recently used entry.
Lookup should also update that entry to be the most recently used entry.
'''