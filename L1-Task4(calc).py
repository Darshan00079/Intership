def addition(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def divison(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def modulus(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x % y

def main():
    print("**********************Simple Calculator**********************")
    print(''' _____________________
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
''')
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operator = input("Enter an operator (+, -, *, /, %): ")

        if operator == '+':
            result = addition(num1, num2)
        elif operator == '-':
            result = subtraction(num1, num2)
        elif operator == '*':
            result = multiplication(num1, num2)
        elif operator == '/':
            result = divison(num1, num2)
        elif operator == '%':
            result = modulus(num1, num2)
        else:
            result = "Invalid operator!"

        print(f"The result is: {result}")
    except ValueError:
        print("Invalid input! Please enter numeric values.")

if __name__ == "__main__":
    main()