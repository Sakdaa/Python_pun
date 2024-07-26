def fire(fbond, fcombust):
    # Step 1: Read bond energy data
    bond_energy = {}
    
    # Open bond energy file
    with open(fbond, 'r') as fb:
        for line in fb:
            parts = line.strip().split()
            if len(parts) == 2:
                bond, energy = parts
                bond_energy[bond] = float(energy)
    
    # Check if bond_energy is populated correctly
    # print(bond_energy)

    # Step 2: Read reaction data
    with open(fcombust, 'r+') as fc:
        # Read the header (ignore it)
        fc.readline()
        
        # Read reactant and product lines
        reactant_line = fc.readline().strip()
        product_line = fc.readline().strip()
        
        # Process reactants
        reactants = reactant_line.split('+')
        E1 = 0
        for r in reactants:
            parts = r.strip().split()
            if len(parts) == 2:
                num_bonds, bond_symbol = parts
                num_bonds = float(num_bonds)
                bond_symbol = bond_symbol.strip()
                E1 += bond_energy.get(bond_symbol, 0) * num_bonds
        
        # Process products
        products = product_line.split('+')
        E2 = 0
        for p in products:
            parts = p.strip().split()
            if len(parts) == 2:
                num_bonds, bond_symbol = parts
                num_bonds = float(num_bonds)
                bond_symbol = bond_symbol.strip()
                E2 += bond_energy.get(bond_symbol, 0) * num_bonds
        
        # Calculate the activation energy, releasing energy, and their difference
        total_E = E1 - E2
        msg = '\nEa = {:,.1f} kJ, Er = {:,.1f} kJ, E = {:,.1f} kJ'.format(E1, E2, total_E)
        
        # Append result to the end of the combustion file
        fc.write(msg)
if __name__ == '__main__':
    fire('bond_energy.txt', 'methane.txt')
