cash_savings = float(input("Enter your total cash savings: "))
gold_value = float(input("Enter the total value of your gold: "))
inventory_value = float(input("Enter the value of your business inventory: "))

total_wealth = cash_savings + gold_value + inventory_value
zakat_due = total_wealth * 0.025

print(f"Total Zakatable Wealth: {total_wealth:,.2f}")
print(f"Zakat Due (2.5%): {zakat_due:,.2f}")