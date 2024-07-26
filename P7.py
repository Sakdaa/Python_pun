#P7
import math

def Hipparchus(do, theta_m):
    # Compute the estimated distance to the moon Dm
    Dm = (do / 2) * math.tan(math.radians(theta_m))
    
    # Compute the range bounds if the measure is off by 0.01 degrees
    Dm_lower = (do / 2) * math.tan(math.radians(theta_m - 0.01))
    Dm_upper = (do / 2) * math.tan(math.radians(theta_m + 0.01))
    
    # Ensure Dml < Dmu
    Dml, Dmu = min(Dm_lower, Dm_upper), max(Dm_lower, Dm_upper)
    
    return Dm, Dml, Dmu
def Aristarchus(dm, theta_s):
    # Compute the estimated distance to the sun Ds
    Ds = dm / math.tan(math.radians(theta_s))
    
    # Compute the range bounds if the measure is off by 0.01 degrees
    Ds_lower = dm / math.tan(math.radians(theta_s + 0.01))
    Ds_upper = dm / math.tan(math.radians(theta_s - 0.01))
    
    # Ensure Dsl < Dsu
    Dsl, Dsu = min(Ds_lower, Ds_upper), max(Ds_lower, Ds_upper)
    
    return Ds, Dsl, Dsu

if __name__ == "__main__":
    res = Hipparchus(400, 89.97)
    print('Hipparchus:{:,.2f} km; [{:.0f} , {:.0f}] if 0.01 deg off'.format(*res)) 
    res = Aristarchus(381972, 0.15) 
    print('Aristarchus: {:,.2f} km; [{:.0f} , {:.0f}] if 0.01 deg off'.format(*res))