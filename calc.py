def add(x, y):
    return x + y


def subtract(x, y):
    return x - y

def root(x,y):
    if x < 0 and y % 2 == 0:
        raise ValueError("Cannot take even root of a negative number.")
    return x ** (1 / y)

def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y


def calculator():
    print("Simple Calculator")
    print("Operations: +, -, *, /,root")

    while True:
        try:
            num1 = float(input("Enter first number: "))
            op = input("Enter operator (+, -, *, /, root): ")
            num2 = float(input("Enter second number: "))

            if op == '+':
                result = add(num1, num2)
            elif op == '-':
                result = subtract(num1, num2)
            elif op == '*':
                result = multiply(num1, num2)
            elif op == '/':
                result = divide(num1, num2)
            elif op == 'root':
                result = root(num1, num2)
            else:
                print("Invalid operator!")
                continue

            print(f"Result: {result}")

        except ValueError as e:
            print(f"Invalid input: {e}")
        except Exception as e:
            print(f"Error: {e}")

        again = input("Do you want to continue? (y/n): ").strip().lower()
        if again != 'y':
            print("Goodbye!")
            break


if __name__ == "__main__":
    calculator()
