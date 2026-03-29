def calculate_area(length, width):
    return length * width

def calculate_perimeter(length, width):
    return 2 * (length + width)

rect_length = float(input("Enter the length of the rectangle: "))
rect_width = float(input("Enter the width of the rectangle: "))

area = calculate_area(rect_length, rect_width)
perimeter = calculate_perimeter(rect_length, rect_width)

print(f"Rectangle Area: {area}")
print(f"Rectangle Perimeter: {perimeter}")