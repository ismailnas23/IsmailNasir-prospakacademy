user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))
height_cm = float(input("Enter your height in centimeters: "))
is_student = input("Are you a student? (Type 'True' or 'False'): ")

height_inches = height_cm / 2.54

print("\n--- User Profile ---")
print(f"Name: {user_name}")
print(f"Age: {user_age} years")
print(f"Height: {height_cm} cm ({height_inches:.2f} inches)")
print(f"Student: {is_student}")