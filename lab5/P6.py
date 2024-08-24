import numpy as np

# Objective function
def objective(v):
    return 5 * v - 3 * (1 - np.log(3.8 - v)) - 1

# Gradient of the objective function
def dPv(v):
    return 5 - (3 / (3.8 - v))

# Maximizer function using gradient ascent
def maximizer(initial_v, step_size, num_steps):
    v = initial_v
    for _ in range(num_steps):
        gradient = dPv(v)
        v += step_size * gradient  # Update v based on the gradient
        # Ensure v stays within bounds (0, 3.7)
        if v < 0:
            v = 0
        elif v > 3.7:
            v = 3.7
    return v

if __name__ == "__main__": 
    v = 1.2 
    print('objective=', objective(v)) 
    print('dPv=', dPv(v)) 
    print('v*=', maximizer(v, 0.001, 100)) 
    print('v*=', maximizer(v, 0.01, 10)) 
    print('v*=', maximizer(v, 0.02, 10)) 
