data_file = "inventory.txt"

def parse_inventory(filename):
    items = []
    try:
        with open(filename, "r") as file:
            for line in file:
                try:
                    parts = line.strip().split(",")
                    name = parts[0]
                    price = float(parts[1])
                    quantity = int(parts[2])
                    items.append({"name": name, "price": price, "quantity": quantity})
                except (ValueError, IndexError):
                    print(f"Warning: Skipping invalid data row: {line.strip()}")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    return items

inventory_data = parse_inventory(data_file)

if inventory_data:
    total_value = 0
    print("\n--- Current Inventory ---")
    for item in inventory_data:
        item_total = item["price"] * item["quantity"]
        total_value += item_total
        print(f"Product: {item['name']} | Price: ${item['price']:.2f} | Qty: {item['quantity']} | Value: ${item_total:.2f}")
    
    print("-" * 30)
    print(f"Total Inventory Value: ${total_value:.2f}")