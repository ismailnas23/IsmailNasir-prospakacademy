while True:
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 / num2
    except ValueError:
        print("Error: Invalid input. Please enter numeric values.")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    else:
        print(f"The result of {num1} divided by {num2} is {result}")
    finally:
        calculation_status = input("Do you want to perform another calculation? (yes/no): ").lower()
        if calculation_status != 'yes':
            break