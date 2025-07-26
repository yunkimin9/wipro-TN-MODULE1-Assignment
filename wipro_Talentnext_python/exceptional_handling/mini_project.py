
'''  Project-1
Q-> You had saved the items and their price details in a text file. which you purchased yesterday from a nearnby super market
  '''

def main():
    try:
        
        filename = input("Enter the file name (without .txt): ").strip() + ".txt"

        with open(filename, 'r', encoding='utf-8') as file:
            lines = [line.strip() for line in file if line.strip()]  

        purchased_items = 0
        free_items = 0
        total_amount = 0
        discount = 0

        for line in lines:
            parts = line.split()

            if len(parts) < 2:
                continue

            item_name = parts[0]
            item_price = parts[1]

            if item_name.lower() == "discount":
                try:
                    discount = int(item_price)
                except ValueError:
                    print("Invalid discount value. Skipping.")
            elif item_price.lower() == "free":
                free_items += 1
            else:
                try:
                    total_amount += int(item_price)
                    purchased_items += 1
                except ValueError:
                    print(f"Invalid price for item '{item_name}'. Skipping.")

        final_amount = total_amount - discount

        print(f"No of items purchased: {purchased_items}")
        print(f"No of free items: {free_items}")
        print(f"Amount to pay: {total_amount}")
        print(f"Discount given: {discount}")
        print(f"Final amount paid: {final_amount}")

    except FileNotFoundError:
        print("File not found. Please check the name and try again.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()