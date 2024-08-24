# Define the table as a dictionary with tuples as keys
g_u = {
    (-5, -8): 6,
    (-5, 6): 7.2,
    (-5, 7.2): 0.4,
    (-5, 0.4): -0.11,
    (-3, -4): 7,
    (-3, 7): 12,
    (-3, 12): 8,
    (-3, -0.3): -2.3,
    (0, 0): 2.1,
    (0, 5.4): 4,
    (0, 4): 2.1,
    (0, -17): -17,
    (3, -9): -24,
    (3, -16): 8,
    (3, 2.1): 2.1,
    (3, 1.9): 0.4,
    (5, 0): -9,
    (5, -1): -2
}

# Helper function to calculate the argmin or argmax for multi-dimensional u
def argmin_g_u(func):
    return min(g_u, key=func), func(min(g_u, key=func))

def argmax_g_u(func):
    return max(g_u, key=func), func(max(g_u, key=func))

# Q2.1: v = argmin_u g(u)
v_2_1, g_v_2_1 = argmin_g_u(lambda u: g_u[u])
print(f"Q2.1. v = {v_2_1} ; OVO = {g_v_2_1} ; g(v) = {g_v_2_1}")

# Q2.2: v = argmin_u |g(u)|
v_2_2, g_v_2_2 = argmin_g_u(lambda u: abs(g_u[u]))
print(f"Q2.2. v = {v_2_2} ; OVO = {abs(g_v_2_2)} ; g(v) = {g_v_2_2}")

# Q2.3: v = argmax_u g(u)
v_2_3, g_v_2_3 = argmax_g_u(lambda u: g_u[u])
print(f"Q2.3. v = {v_2_3} ; OVO = {g_v_2_3} ; g(v) = {g_v_2_3}")

# Q2.4: v = argmax_u g(-u)
v_2_4, g_v_2_4 = argmax_g_u(lambda u: g_u.get((-u[0], -u[1]), float('-inf')))
print(f"Q2.4. v = {(-v_2_4[0], -v_2_4[1])} ; OVO = {g_v_2_4} ; g(v) = {g_v_2_4}")

# Q2.5: v = argmin_u (g(u)-9)
v_2_5, g_v_2_5 = argmin_g_u(lambda u: abs(g_u[u] - 9))
print(f"Q2.5. v = {v_2_5} ; OVO = {g_u[v_2_5]} ; g(v) = {g_v_2_5}")
