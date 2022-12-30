def decimalToBinary(testVariable):
    # Base Case
    if testVariable <= 1:
        return str(testVariable)
    # Recursive Case
    else:
        return decimalToBinary(testVariable // 2) + decimalToBinary(testVariable % 2)
"""
To convert a decimal number to a binary number, keep track of the remainder and 
the remaining dividend when the number is divided by 2. 
We continue dividing the number by 2 until we are left with 1


"""