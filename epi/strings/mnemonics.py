'''
Write a program which takes as input a phone number,
specified as a string of digits, and returns all possible
character sequences that correspond to the phone number.
The cell phone keypad is specified by a mapping that takes
a digit and returns the corresponding set of characters.
The character sequences do not have to be legal words or 
phrases.
'''
def computeMnemonics(phoneNumber):
    # mapping of number to characters
    numbers = {
            "0": "",
            "1": "",
            "2": "ABC",
            "3": "DEF",
            "4": "GHI",
            "5": "JKL",
            "6": "MNO",
            "7": "PQRS",
            "8": "TUV",
            "9": "WXYZ"
            }
    p = []
    def gen(i,poss):
        if i >= len(phoneNumber):
            # we've reached the end of the phone number
            p.append(str(poss))
            return
        # let's explore the current number
        for char in numbers[phoneNumber[i]]:
            # add each character to the current state of the possibility string
            gen(i+1,poss+char)

    gen(0, "")
    return p

print(computeMnemonics("22"))
