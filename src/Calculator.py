print("Welcome to PyCalculator!")
num1 = int(input("num1: "))
op = input("Operator: ")
num2 = int(input("num2: "))

while True:
    if op == "+":
        num3 = num1 + num2
    elif op == "-":
        num3 = num1 - num2
    elif op == "/":
        num3 = num1 / num2
    elif op == "*":
        num3 = num1 * num2
    elif op == "reset":
        continue
    elif op == "close":
        break
    else:
        print("Invalid Operator")
        op = input("Operator: ")
        continue

    print(num1,op,num2,'=',num3)
    num1 = num3
    print('num1:', num1)
    op = input("Operator: ")
    if op == "close":
        break
    num2 = int(input("num2: "))


    