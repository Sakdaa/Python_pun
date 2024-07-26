def factorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def power_series_exponential(x, M):
    s = 0
    for n in range(M + 1):
        s += (x ** n) / factorial(n)
    return s

if __name__ == "__main__":
    # Interaction example
    x = float(input("x: "))
    M = int(input("M: "))

    s = power_series_exponential(x, M)
    print("s = {:.5f}".format(s))
