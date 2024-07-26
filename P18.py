def calculate_landfill_size(daily_waste_per_person, holding_capacity_per_m2):
    population_size = 70000000  # 70 million people
    days_per_year = 365
    square_meters_per_rai = 1600
    
    # Calculate total daily waste in kg
    total_daily_waste = daily_waste_per_person * population_size
    
    # Calculate land size needed for daily waste in m2
    land_size_daily_m2 = total_daily_waste / holding_capacity_per_m2
    
    # Convert land size from m2 to rai
    land_size_daily_rai = land_size_daily_m2 / square_meters_per_rai
    
    # Calculate land size needed for yearly waste in rai
    total_yearly_waste = total_daily_waste * days_per_year
    land_size_yearly_m2 = total_yearly_waste / holding_capacity_per_m2
    land_size_yearly_rai = land_size_yearly_m2 / square_meters_per_rai
    
    return total_daily_waste, land_size_daily_rai, land_size_yearly_rai

if __name__ == "__main__":
    # Interaction example
    daily_waste_per_person = float(input("Waste: "))
    holding_capacity_per_m2 = float(input("Cap: "))

    total_daily_waste, land_size_daily_rai, land_size_yearly_rai = calculate_landfill_size(daily_waste_per_person, holding_capacity_per_m2)

    print("Total waste= {:.2f}".format(total_daily_waste))
    print("Landfill= {:.2f}".format(land_size_daily_rai))
    print("Annual land= {:.2f}".format(land_size_yearly_rai))
