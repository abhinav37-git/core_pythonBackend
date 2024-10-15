num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
op = input("Enter the operator: ")

def calculator(num1, num2, op):
    
    if op == "+":
        result = num1+num2
    elif op == "-":
        result = num1-num2
    elif op == "*":
        result = num1*num2
    elif op == "/":
        result = num1/num2
    elif op == "ˆ":
        result = num1**num2
    
    print("The result is", result)
    return result

calculator(num1, num2, op)