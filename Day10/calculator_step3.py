# Add
def add(n1, n2) :
    return n1 + n2

# Subtract
def subtract(n1, n2) :
    return n1 - n2

# Multiply
def multiply(n1, n2) :
    return n1 * n2

# Divide
def divide(n1, n2) :
    return n1 / n2

# Create a dictionary named operations
operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

# Calculator
num1 = int(input("What's the first number?: "))

for symbol in operations :
    print(symbol)

should_continue = True

while should_continue :
    # operation_symbol = input("Pick an operation from the line above: ")
    operation_symbol = input("Pick an operation: ")

    # num2 = int(input("What's the second number?: "))
    num2 = int(input("What's the next number?: "))

    calculation_function = operations[operation_symbol]
    # first_answer = calculation_function(num1, num2)
    answer = calculation_function(num1, num2)

    # print(f"{num1} {operation_symbol} {num2} = {first_answer}")
    print(f"{num1} {operation_symbol} {num2} = {answer}")

    # + another operation

    # new_operation_symbol = input("Pick another operation: ")
    # num3 = int(input("What's the next number?: "))
    # new_calculation_function = operations[new_operation_symbol]
    # second_answer = new_calculation_function(calculation_function(num1, num2), num3)
    # print(f"{first_answer} {new_operation_symbol} {num3} = {second_answer}")

    if input(f"Type 'y' to continue calculation with {answer}, or type 'n' to exit.: ") == 'y' :
        num1 = answer
    else :
        should_continue = False