import math

number = float(input("Enter a number to find its square root: "))
result_sqrt = math.sqrt(number)
print(f"The square root of {number} is {result_sqrt}")

base = float(input("Enter the base number: "))
exponent = float(input("Enter the exponent: "))
result_pow = math.pow(base, exponent)
print(f"{base} raised to the power of {exponent} is {result_pow}")