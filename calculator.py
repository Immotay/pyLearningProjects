# ---------------------#
#  OPERATION FUNCTIONS #
# ---------------------#

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def div(x, y):
    return x / y

def mul(x, y):
    return x * y

# ---------------------#
# AVAILABLE OPERATIONS #
# ---------------------#

operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}

# --------------------------#
# USER-INTERACTED FUNCTIONS #
# --------------------------#

def get_n1():
    """asks user for the first input"""
    return float(input('Type out the first number: '))

def get_n2():
    """asks user for the second input"""
    return float(input('Type out the second number: '))

def get_ops():
    """presents user with a list of operations
    + - * /
    and asks it to choose one"""
    print('----AVAILABLE OPERATIONS----')
    for k in operations:
        print(k)
    selected = input('Select an operation from the above list: ')
    while selected not in operations:
        selected = input('Please select a valid operation (+, -, * or /): ')
    return selected

# ---------------------#
#    STARTING VALUES   #
# ---------------------#

calculations = 0
keep_going = True

# --------------------- #
#          CORE         #
# --------------------- #

while keep_going:
    if calculations == 0:
        n1 = get_n1()
    else:
        n1 = result
    op = get_ops()
    n2 = get_n2()
    result = operations[op](n1, n2)
    print(f'{n1} {op} {n2} = {result}')
    calculations += 1
    question = input(f'Type "y" to keep performing calculations with {result}, "n" to start a new one or "q" to quit: ').lower()
    if question == 'n':
        print(f'\n' * 20)
        calculations = 0
    elif question != 'y':
        keep_going = False