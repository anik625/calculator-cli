# calculator.py
# Simple Python Calculator (CLI)

def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

print("Select operation: 1.Add  2.Subtract  3.Multiply  4.Divide")
choice = input("Enter choice (1/2/3/4): ")

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if choice == "1":
    print("Result:", add(a, b))
elif choice == "2":
    print("Result:", subtract(a, b))
elif choice == "3":
    print("Result:", multiply(a, b))
elif choice == "4":
    print("Result:", divide(a, b))
else:
    print("Invalid Input")
