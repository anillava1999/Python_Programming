print("Welcome to the calclualtor")

def add(A, B):
    Result = A + B
    return Result

def minus(A,B):
    Result = A - B
    return Result

def multiply(A, B):
    Result = A * B
    return Result

def divide(A, B):
    Result = A / B
    return Result

def functions(A,B):
    if element == '+':
        Result = add(A,B)
    elif element == '-':
        Result = minus(A,B)
    elif element == '*':
        Result = multiply(A,B)
    elif element == '/':
        Result = divide(A,B)
    return Result



k = 0
A = int(input('Enter the number  '))
B = int(input('Enter the number  '))
element = input('Enter the Mathematical Symbol (+,-,*, /) ')
output = functions(A,B)
A = output
print(output)

while True:
    B = input('Enter the number  ')

    if B != 'Result':
        B = int(B)
        element = input('Enter the Mathematical Symbol (+,-,*, /) ')
        output_con = functions(A,B)
        A = output_con
    elif B == 'Result':
        print(output_con)
        break


