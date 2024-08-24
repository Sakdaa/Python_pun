# import numpy as np
# from scipy.optimize import minimize_scalar

# # Define the power function P(v)
# def P(v):
#     return 5*v - 3*(1 - np.log(3.8 - v))**-1

# # Find the maximum of P(v) within the interval (0, 3.7) with higher precision
# result = minimize_scalar(lambda v: -P(v), bounds=(0, 3.7), method='bounded', options={'xatol': 1e-6})

# # Extract the optimal voltage and the corresponding maximum power
# v_star = result.x
# P_max = P(v_star)

# # Display the results for Q3.1
# print(f"Q3.1. v = {v_star:.3f} volt and P(v) = {P_max:.3f} watt")

# # Define load requirements
# load_10_watt = 10
# load_20_watt = 20
# safety_margin = 1.2  # 20% margin

# # Check if one panel is sufficient for a 10-watt load
# if P_max >= load_10_watt:
#     print(f"Q3.2. Yes. We need 1 panel(s).")
# else:
#     panels_needed_10 = int(np.ceil(load_10_watt / P_max))
#     print(f"Q3.2. No. We need {panels_needed_10} panel(s).")

# # Check if one panel is sufficient for a 20-watt load
# if P_max >= load_20_watt:
#     print(f"Q3.3. Yes. We need 1 panel(s).")
# else:
#     panels_needed_20 = int(np.ceil(load_20_watt / P_max))
#     print(f"Q3.3. No. We need {panels_needed_20} panel(s).")

# # Check if one panel is sufficient for a 20-watt load with a safety margin
# required_power_with_margin = load_20_watt * safety_margin
# if P_max >= required_power_with_margin:
#     print(f"Q3.4. Yes. We need 1 panel(s).")
# else:
#     panels_needed_margin = int(np.ceil(required_power_with_margin / P_max))
#     print(f"Q3.4. No. We need {panels_needed_margin} panel(s).")
import numpy as np
from scipy.optimize import minimize_scalar

# Define the power function P(v)
def P(v):
    return 5*v - 3*(1 - np.log(3.8 - v)) - 1  # Corrected power function

# Find the maximum of P(v) within the interval (0, 3.7) with higher precision
result = minimize_scalar(lambda v: -P(v), bounds=(0, 3.7), method='bounded', options={'xatol': 1e-6})

# Extract the optimal voltage and the corresponding maximum power
v_star = result.x
P_max = P(v_star)

# Display the results for Q3.1
print(f"Q3.1. v = {v_star:.3f} volt and P(v) = {P_max:.3f} watt")

# Define load requirements
load_10_watt = 10
load_20_watt = 20
safety_margin = 1.2  # 20% margin

# Check if one panel is sufficient for a 10-watt load
if P_max >= load_10_watt:
    print(f"Q3.2. Yes. We need 0 panel(s).")  # One panel is enough
else:
    panels_needed_10 = int(np.ceil(load_10_watt / P_max))
    print(f"Q3.2. No. We need {panels_needed_10} panel(s).")

# Check if one panel is sufficient for a 20-watt load
if P_max >= load_20_watt:
    print(f"Q3.3. Yes. We need 0 panel(s).")  # One panel is enough
else:
    panels_needed_20 = int(np.ceil(load_20_watt / P_max))
    print(f"Q3.3. No. We need {panels_needed_20} panel(s).")

# Check if one panel is sufficient for a 20-watt load with a safety margin
required_power_with_margin = load_20_watt * safety_margin
if P_max >= required_power_with_margin:
    print(f"Q3.4. Yes. We need 0 panel(s).")  # One panel is enough
else:
    panels_needed_margin = int(np.ceil(required_power_with_margin / P_max))
    print(f"Q3.4. No. We need {panels_needed_margin} panel(s).")
