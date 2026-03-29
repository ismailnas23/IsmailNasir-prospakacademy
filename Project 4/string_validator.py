raw_string = input("Enter a string to process: ")
clean_string = raw_string.strip()

if len(clean_string) > 0:
    print(f"Original: '{raw_string}'")
    print(f"Cleaned: '{clean_string}'")
    print(f"Uppercase: {clean_string.upper()}")
    print(f"Lowercase: {clean_string.lower()}")
    print(f"Is Alphanumeric: {clean_string.isalnum()}")
    print(f"Character Count: {len(clean_string)}")
else:
    print("The string is empty or contains only whitespace.")