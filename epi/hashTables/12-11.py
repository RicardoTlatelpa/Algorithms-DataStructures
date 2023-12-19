'''
The Collatz conjecture is the following:
    Take any natural number.
    if it is odd, triple it and add one
    if it is even, halve it
    Repeat the process indefinitely.
No matter what number you begin with, you will eventually
arrive at 1.

If we start with 11 we get the sequence
34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1
'''

def test_collatz_conjecture(n):
    verified_numbers = set()
    for i in range(3,n+1):
        sequence = set()
        test_i = i
        while test_i >= i:
            if test_i in sequence:
                return False
            sequence.add(test_i)
        if test_i % 2:
            if test_i in verified_numbers:
                break
            verified_numbers.add(test_i)
            test_i = 3 * test_i + 1
        else:
            test_i //= 2 # even number, halve it 
    return True
