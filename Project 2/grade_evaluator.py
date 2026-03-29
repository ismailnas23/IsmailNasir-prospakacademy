score = int(input("Enter the student's numerical score (0-100): "))

if score < 0 or score > 100:
    print("Invalid score.")
else:
    if score >= 90:
        print("The grade is: A")
    elif score >= 80:
        print("The grade is: B")
    elif score >= 70:
        print("The grade is: C")
    elif score >= 60:
        print("The grade is: D")
    else:
        print("The grade is: F")