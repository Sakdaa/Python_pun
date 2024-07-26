def calculate_energy_per_volume(fuel_density, calorific_value):
    # Constants
    LITERS_PER_BARREL = 158.987

    # Calculate energy per liter
    energy_per_liter = fuel_density * calorific_value

    # Calculate energy per barrel
    energy_per_barrel = energy_per_liter * LITERS_PER_BARREL

    return energy_per_liter, energy_per_barrel

def main():
    # Input fuel density and calorific value
    fuel_density = float(input("Fuel density (in kg/L): "))
    calorific_value = float(input("Calorific value (in MJ/kg): "))

    # Calculate energy per volume
    energy_per_liter, energy_per_barrel = calculate_energy_per_volume(fuel_density, calorific_value)

    # Print results
    print("This fuel has energy per volume of {:.2f} MJ/L.".format(energy_per_liter))
    print("That is {:.2f} MJ/bbl.".format(energy_per_barrel))


if __name__ == '__main__':
    main()
