#P5
def mighty_river(river_info):
    river_power = {}
    
    for river, info in river_info.items():
        A = info[0]  # Cross-section area in m^2
        rho = info[1]  # Water density in kg/m^3
        Q = info[2]  # Flow rate in m^3/s
        
        P = (1/(2*(A **2))) * rho *(Q ** 3)
        
        # Store the calculated power in the result dictionary
        P_rounded = round(P, 4)
        river_power[river] = P_rounded
    
    return river_power

# Example usage:
mighties = {'Amazon': [1.2e6, 1100, 210000],
 'Congo': [2e6, 1150, 41200], 
 'Yangtze': [800e3, 1200, 30000]}

if __name__ == "__main__":
    river_power = mighty_river(mighties)
    print(river_power)
