'''

Test class.

Classes:

Functions:

    add(number, number)

Misc variables:

'''

def add(number1, number2):
    '''Takes two numbers and return it's addition'''
    return number1 + number2

NUM1 = 4
NUM2 = 5
TOTAL = add(NUM1, NUM2)

print("The sum of {} and {} is {}".format(NUM1, NUM2, TOTAL))
