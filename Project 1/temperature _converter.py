celsius_str = input("Enter temperature in Celsius: ")
celsius_value = float(celsius_str)
fahrenheit_value = (celsius_value * 9/5) + 32
print(f"{celsius_value} degrees Celsius is equal to {fahrenheit_value:.1f} degrees Fahrenheit.")