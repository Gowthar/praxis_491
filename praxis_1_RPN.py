'''
PROBLEM:
*RPN Calculator
Author of Solution:
*Zachary Benning
GIVEN PROMPT:
*February 19, 2009
*Implement an RPN calculator that takes an expression like 19 2.14 + 4.5 2 4.3 / - * which
*is usually expressed as
*(19 + 2.14) * (4.5 - 2 / 4.3) and responds with 85.2974.
*The program should read expressions from standard input and
*print the top of the stack to standard output when a newline is encountered.
*The program should retain the state of the operand stack between expressions.
SOLUTION TEST:
* "19 2.14 + 4.5 2 4.3 / - *" = 85.2974
'''

#used to convert string operands to operators
import operator

'''
USER_INPUT_SANITIZER
OUTPUT: user input into workable form
PROCESS: Take input and store it into temp word until another space is entered
            Then push word into workable list and reset word space 
'''
def user_input_sanitizer():
    user_input = input('Please Enter Valid RPN Equation with a single space between each')
    cap = []
    word = ''
    for x in range(len(user_input)):
        word += user_input[x]
        if user_input[x].isspace():
            cap.append(word.strip())
            word = ''
    cap.append(word.strip())
    return cap

'''
SOLVER
INPUT: string of operations and values with no spaces
OUTPUT: Solution
LIBARIES REFERENCED: operator(to handle arbitrary operand string conversion to operators
PROCESS: Declare operators in use, loop through input, solve according to RPN and output sol
'''
def solver(cap):
    #string converter for operands
    ops = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
    # form is as given :: ops['+'](1,1) = 2

    for x in range(len(cap)):
        #check if on operand
        if cap[x] == '+' or cap[x] == '-' or cap[x] == '*' or cap[x] == '/':
            #takes in arbitrary operand and performs calc on previous two terms
            cap[x] = ops[cap[x]](float(cap[x-2]),float(cap[x-1]))
            #removes terms and inserts placeholder at the beginning
            #this is done to eliminate for loop index access errors
            cap.pop(x-1)
            cap.pop(x-2)
            cap.insert(0,'IGN')
            cap.insert(0,'IGN')
    return round(cap[-1],4)


print(solver(user_input_sanitizer()))
