print("Welcome to PyCalculator!")
print("To close calculator type 'close'")
num1 = int(input("num1: "))
op = input("Operator: ")
num2 = int(input("num2: "))

while True:

    if op == "+":
        print(num1 + num2)
    elif op == "-":
        print(num1 - num2)
    elif op == "/":
        print(num1 / num2)
    elif op == "*":
        print(num1 * num2)
    elif op == "close":
        break
    else:
        print("Invalid Operator")

    op = input("Operator: ")


    