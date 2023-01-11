def gcd(n1, n2,divisors):
    if n1 == 0 or n2 == 0 or n1 == 1 or n2 == 1:
        return
    elif n1 > n2:
        divisible = n1 // n2
        remainder = n1 % n2
        if remainder == 0 or remainder == 1:
            return
        divisors.append(remainder)
        gcd(n2, remainder, divisors)
    else:
        divisible = n2 // n1
        remainder = n2 % n1
        if remainder == 0 or remainder == 1:
            return
        divisors.append(remainder)
        gcd(n1, remainder, divisors)

def main():
    i = 718
    j = 193
    divisors = []
    gcd(i,j,divisors)
    print(divisors[len(divisors)-1])
    
main()
