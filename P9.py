def sweet(fsweet, fdrink):
    # Retrieve sweetness dict
    sweetness = {}
    
    # Read sweetness table file and populate the sweetness dictionary
    with open(fsweet, 'r') as file:
        next(file)  # Skip the header
        for line in file:
            parts = line.split()
            if len(parts) >= 2:  # Ensure there are at least two parts
                sweetener = parts[0]
                value = float(parts[1])
                sweetness[sweetener] = value
    
    # Calculate the estimated sweetness
    sweet_sum = 0
    with open(fdrink, 'r') as file:
        for line in file:
            parts = line.split()
            if len(parts) == 2:  # Ensure there are exactly two parts
                sweetener, amount = parts
                try:
                    amount = float(amount)
                    if sweetener in sweetness:
                        sweet_sum += sweetness[sweetener] * amount
                except ValueError:
                    # Handle cases where amount is not a valid float
                    print(f"Skipping line with invalid amount: {line.strip()}")
    
    # Format the message
    msg = "\nSweet as {:.1f}% sucrose solution".format(sweet_sum)
    
    # Write/append message to the end of the drink-sweetener file
    with open(fdrink, 'a') as file:
        file.write(msg)

if __name__ == '__main__':
    sweet('sweetness1.txt', 'CocaPanda.txt')
