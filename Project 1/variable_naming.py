principal_amount = float(input("Enter the principal amount: "))
interest_rate = float(input("Enter the annual interest rate (as a decimal): "))
time_years = int(input("Enter the time in years: "))

total_interest = principal_amount * interest_rate * time_years

print(f"The total interest calculated is: {total_interest:,.2f}")