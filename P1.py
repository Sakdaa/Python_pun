#P1
import math

def cos_sim(a, b):
    # Compute the dot product of a and b
    dot_product = sum([ai * bi for ai, bi in zip(a, b)])
    
    # Compute the magnitude of vector a
    mag_a = math.sqrt(sum([ai**2 for ai in a]))
    
    # Compute the magnitude of vector b
    mag_b = math.sqrt(sum([bi**2 for bi in b]))
    
    # Handle division by zero edge case
    if mag_a == 0 or mag_b == 0:
        return 0
    
    # Compute the cosine similarity
    similarity = dot_product / (mag_a * mag_b)
    
    return similarity

if __name__ == "__main__":
# Example usage:
    # cs = cos_sim([1, 0], [5, 5])
    # print(cs)

    cs = cos_sim([14, 0, 5], [5, 8, 4])
    print(cs)