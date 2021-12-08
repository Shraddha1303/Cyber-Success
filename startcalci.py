# operation def fuction
def add(a, b):
    print(f"{a + b}")


def Subtract(a, b):
    print(f"{a - b}")


def multiply(a, b):
    print(f"{a * b}")


def power(a, b):
    print(f"{a ** b}")


# calci def function
def calci(x, y, op):
    if op == "+":
        return add(x, y)
    elif op == "-":
        return Subtract(x, y)
    elif op == "*":
        return multiply(x, y)
    elif op == "**":
        return power(x, y)
    else:
        print("Enter operator to perform")

    # start program


def abc(x, y):
    print(f"{'*' * x}{y}{'*' * x}")


abc(4, "Start the Program")

p = input("Enter the operator sign ")
var = int(input("enter 1st number "))
var1 = int(input("enter 2nd number "))
print("The Answer is", end=" ")
calci(var, var1, p)


# end program
def abc(x, y):
    print(f"{'*' * x}{y}{'*' * x}")


abc(4, "Stop the Program")