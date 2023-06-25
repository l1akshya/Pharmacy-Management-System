import csv

def generate_bill(csv_file, bill_file):
    # Open the CSV file
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        # Skip the header row
        next(reader)  
        # Initialize variables
        total_amount = 0
        bill_contents = []
        # Read the contents from the CSV file
        for row in reader:
            item = row[0]
            quantity = 1
            price = float(row[4])
            # Calculate the total amount for each item
            item_total = quantity * price
            total_amount += item_total    
            # Add the item details to the bill contents
            bill_contents.append(f"{item} - {quantity} x {price:.2f} = {item_total:.2f}")
    
    # Generate the bill in a text file
    with open(bill_file, 'w') as file:
        file.write("-------- Bill --------\n")
        file.write('\n'.join(bill_contents))
        file.write(f"\nTotal Amount: {total_amount:.2f}")
        file.write("\n----------------------\n")
        file.write("Thank you for your purchase!")

