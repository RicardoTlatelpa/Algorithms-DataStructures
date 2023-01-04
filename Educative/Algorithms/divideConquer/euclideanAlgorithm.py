divisors = []
def gcd(n1, n2):
    print(n1,n2)
    if n1 == 0 or n2 == 0 or n1 == 1 or n2 == 1:
        return
    elif n1 > n2:
        divisible = n1 // n2
        remainder = n1 % n2
        divisors.append(remainder)
        gcd(n2, remainder)
    else:
        divisible = n2 // n1
        remainder = n2 % n1
        divisors.append(remainder)
        gcd(n1, remainder)
gcd(1575, 231)
size = len(divisors)
n1 = 1575 / divisors[size - 2]
n2 = 231 / divisors[size - 2]
print(n1,n2)
