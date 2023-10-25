'''
A string is said to be an arithmetical expression in Reverse Polish notation(RPN) if:
    (1.) It is a single digit or a sequence of digits, prefixed with an option -, e.g., 
    "6", "123", "-42".
    (2.) It is of the form "A,B, o" where A and B are RPN expressions and o is one of
    +,-,X,/.
'''

def rpn(expression):
    # parse the expression, split by ','
    io = expression.split(',')
    stack = [] # store all the numbers I find
    for char in io:
        if char == '+' or char == '-' or char == 'X' or char == '/':
            n2 = stack.pop()
            n1 = stack.pop()
            new_num = 0
            if char == '+':
                new_num = n1 + n2
            if char == '-':
                new_num = n1 - n2
            if char == 'X':
                new_num = n1 * n2
            if char == '/':
                new_num = n1 / n2
            stack.append(new_num)
        else:
            stack.append(int(char))
    return stack[-1]

print(rpn("3,4,+,2,X,1,+"))

def evaluate(RPN_expression):
    intermediate_results = []
    DELIMITER = ','
    OPERATORS = {
            '+': lambda y, x: x + y,
            '-': lambda y, x: x - y,
            '*': lambda y, x: x * y,
            '/': lambda y, x: int(x/y)
    }
    for token in RPN_expression.split(DELIMITER):
        if token in OPERATORS:
            intermediate_results.append(OPERATORS[token](intermediate_results.pop(), intermediate_results.pop()))
        else: # token is a number
            intermediate_results.append(int(token))
    return intermediate_results[-1]

'''
Since we perform O(1) computation per character of the string, the time complexity is O(n),
where n is the length of the string
'''
