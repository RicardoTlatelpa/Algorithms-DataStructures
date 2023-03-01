'''
Write a function that computes the list
of the first 100 Fibonacci numbers. The 
first two Fibonacci numbers are 1 and 1.
The n+1-st Fibonacci number can be computed by
adding the n-th and the n-1th Fibonacci number
The first few are there 1,1,
1 + 1 = , 1 + 2 = 3, 2 + 3 = 5, 3+5 = 8
'''

def fib(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        next_sequence = fib(n-1) + fib(n-2)
        print(n,next_sequence)
        return next_sequence

fib(9)
