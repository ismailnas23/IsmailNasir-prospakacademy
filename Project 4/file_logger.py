file_name = "user_log.txt"

user_note = input("Enter a note to save to the file: ")

try:
    with open(file_name, "a") as file:
        file.write(user_note + "\n")
    print("Note successfully saved.")
except IOError:
    print("Error: Could not write to the file.")

try:
    with open(file_name, "r") as file:
        content = file.read()
        print("\n--- Current File Content ---")
        print(content)
except FileNotFoundError:
    print("Error: The file does not exist yet.")