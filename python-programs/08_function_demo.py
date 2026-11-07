def greet(name):
    return f"Hello, {name}! Welcome to Python programming."


def add_numbers(a, b):
    return a + b


def find_square(number):
    return number ** 2


def main():
    print("===== PYTHON FUNCTION DEMONSTRATION =====")

    name = input("Enter your name: ")
    print(greet(name))

    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    print("Sum:", add_numbers(a, b))
    print("Square of first number:", find_square(a))


if __name__ == "__main__":
    main()