students = {
    "101": {"name": "Alice", "age": 20, "grade": "A"},
    "102": {"name": "Bob", "age": 22, "grade": "B"},
    "103": {"name": "Charlie", "age": 21, "grade": "C"}
}

search_id = input("Enter Student ID to search: ")

if search_id in students:
    student_info = students[search_id]
    print(f"Name: {student_info['name']}")
    print(f"Age: {student_info['age']}")
    print(f"Grade: {student_info['grade']}")
else:
    print("Student ID not found.")