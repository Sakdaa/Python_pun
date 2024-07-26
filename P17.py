def carbon_14_dating(starting_ratio, sensitivity):
    current_ratio = starting_ratio
    years = 0
    
    while current_ratio >= sensitivity:
        print("Year {}: ratio = {}".format(years,round(current_ratio, 8)))
        current_ratio *= 0.5
        years += 5730

if __name__ == "__main__":
    # Interaction example
    starting_ratio = int(input("ratio: "))
    sensitivity = float(input("sensitivity: "))

    carbon_14_dating(starting_ratio, sensitivity)
