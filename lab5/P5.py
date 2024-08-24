import numpy as np

def loss(u):
    return (u - 1.5)**2 - 3 * np.log(u + 2)

def grad(u):
    return 2 * (u - 1.5) - 3 / (u + 2)

def minimizer(u, step_size, num_steps):
    for _ in range(num_steps):
        gradient = grad(u)
        u = u - step_size * gradient
    return u

if __name__ == "__main__":
    u = 1
    print('loss=', loss(u))
    print('grad=', grad(u))
    print('minimizer=', minimizer(u, 0.1, 10))
    print('minimizer=', minimizer(u, 0.3, 10))
    print('minimizer=', minimizer(u, 0.9, 10))
    print('minimizer=', minimizer(u, 0.3, 100))