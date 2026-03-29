contacts = {}

while True:
    print("\n1. Add Contact")
    print("2. Search Contact")
    print("3. Display All")
    print("4. Exit")
    
    choice = input("Choose an option: ")
    
    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        contacts[name] = phone
    elif choice == "2":
        search_name = input("Enter name to search: ")
        if search_name in contacts:
            print(f"Phone: {contacts[search_name]}")
        else:
            print("Contact not found.")
    elif choice == "3":
        for name, phone in contacts.items():
            print(f"Name: {name}, Phone: {phone}")
    elif choice == "4":
        break
    else:
        print("Invalid choice.")