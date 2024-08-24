# Define the table as a dictionary
g_u = {
    -5: 13, -4.5: 14, -4: 13, -3.5: 9, -3: 4, -2.5: -4, -2: 0,
    -1.5: -2, -1: -8, -0.5: -14, 0: -19, 0.5: -21, 1: -8, 1.5: -2,
    2: 0.5, 2.5: 4, 3: 5, 3.5: 9, 4: 11, 4.5: 10, 5: 7
}

# Helper function to calculate the argmin or argmax
def argmin_g_u(func):
    return min(g_u, key=func), func(min(g_u, key=func))

def argmax_g_u(func):
    return max(g_u, key=func), func(max(g_u, key=func))

# Q1.1: v = argmin g(u)
v_1_1, g_v_1_1 = argmin_g_u(lambda u: g_u[u])
print(f"Q1.1. v = {v_1_1} ; OVO = {g_v_1_1} ; g(v) = {g_v_1_1}")

# Q1.2: v = argmin |g(u)|
v_1_2, g_v_1_2 = argmin_g_u(lambda u: abs(g_u[u]))
print(f"Q1.2. v = {v_1_2} ; OVO = {abs(g_v_1_2)} ; g(v) = {g_v_1_2}")

# Q1.3: v = argmax g(u)
v_1_3, g_v_1_3 = argmax_g_u(lambda u: g_u[u])
print(f"Q1.3. v = {v_1_3} ; OVO = {g_v_1_3} ; g(v) = {g_v_1_3}")

# Q1.4: v = argmax g(-u)
v_1_4, g_v_1_4 = argmax_g_u(lambda u: g_u[-u])
print(f"Q1.4. v = {-v_1_4} ; OVO = {g_v_1_4} ; g(v) = {g_v_1_4}")

# Q1.5: v = argmax -g(u)
v_1_5, g_v_1_5 = argmax_g_u(lambda u: -g_u[u])
print(f"Q1.5. v = {v_1_5} ; OVO = {-g_v_1_5} ; g(v) = {g_u[v_1_5]}")

# Q1.6: v = argmax (5 - g(u))
v_1_6, g_v_1_6 = argmax_g_u(lambda u: 5 - g_u[u])
print(f"Q1.6. v = {v_1_6} ; OVO = {g_v_1_6} ; g(v) = {g_u[v_1_6]}")

# Q1.7: v = argmax g(u-1)
v_1_7, g_v_1_7 = argmax_g_u(lambda u: g_u.get(u-1, float('-inf')))
print(f"Q1.7. v = {v_1_7 + 1} ; OVO = {g_v_1_7} ; g(v) = {g_v_1_7}")

# Q1.8: v = argmax g(0.5 - u)
v_1_8, g_v_1_8 = argmax_g_u(lambda u: g_u.get(0.5 - u, float('-inf')))
print(f"Q1.8. v = {0.5 - v_1_8} ; OVO = {g_v_1_8} ; g(v) = {g_v_1_8}")

# Q1.9: v = argmax -g(0.5 - u)
v_1_9, g_v_1_9 = argmax_g_u(lambda u: -g_u.get(0.5 - u, float('-inf')))
print(f"Q1.9. v = {0.5 - v_1_9} ; OVO = {-g_v_1_9} ; g(v) = {g_u.get(0.5 - v_1_9, None)}")

# Q1.10: v = argmin |0.5 - g(u)|
v_1_10, g_v_1_10 = argmin_g_u(lambda u: abs(0.5 - g_u[u]))
print(f"Q1.10. v = {v_1_10} ; OVO = {abs(0.5 - g_v_1_10)} ; g(v) = {g_v_1_10}")

# Q1.11: v = argmin g(u) s.t. u < -1
v_1_11, g_v_1_11 = argmin_g_u(lambda u: g_u[u] if u < -1 else float('inf'))
print(f"Q1.11. v = {v_1_11} ; OVO = {g_v_1_11} ; g(v) = {g_v_1_11}")

# Q1.12: v = argmax g(u) s.t. -2.5 ≤ u < 2
v_1_12, g_v_1_12 = argmax_g_u(lambda u: g_u[u] if -2.5 <= u < 2 else float('-inf'))
print(f"Q1.12. v = {v_1_12} ; OVO = {g_v_1_12} ; g(v) = {g_v_1_12}")
