import math  


def power(base, exponent):
    result = base ** exponent
    return result


def square_root(number):
    result = math.sqrt(number)
    return result


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


num1 = int(input("Enter base number: "))
num2 = int(input("Enter exponent: "))
num3 = int(input("Enter number for square root: "))
num4 = int(input("Enter number for factorial: "))


print("Power:", power(num1, num2))
print("Square Root:", square_root(num3))
print("Factorial:", factorial(num4))