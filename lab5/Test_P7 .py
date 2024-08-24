import numpy as np

def loss(A, b, uvec):
    """Calculate the loss function L(u)."""
    return float(uvec.T @ A @ uvec + b.T @ uvec)

def grad(A, b, uvec):
    """Calculate the gradient of the loss function L(u)."""
    return 2 * A @ uvec + b

def line_search(f, grad_f, x, p, alpha0=1.0, rho=0.5, c=0.1):
    """
    Performs line search to find the optimal step size alpha.

    Args:
        f: Objective function
        grad_f: Gradient of the objective function
        x: Current point
        p: Search direction
        alpha0: Initial step size
        rho: Contraction factor
        c: Sufficiency condition parameter

    Returns:
        Optimal step size alpha
    """
    alpha = alpha0
    while f(x + alpha * p) > f(x) + c * alpha * np.dot(grad_f(x), p):
        alpha *= rho
    return alpha

def minimizer(A, b, u0, lr, max_iter, tol=1e-6, use_line_search=False):
    """Run the gradient descent algorithm."""
    uvec = u0.copy()
    for _ in range(max_iter):
        grad_u = grad(A, b, uvec)
        if np.linalg.norm(grad_u) < tol:
            break
        if use_line_search:
            alpha = line_search(loss, grad, uvec, -grad_uvec)
            uvec += alpha * (-grad_uvec)
        else:
            uvec -= lr * grad_uvec
    return uvec

if __name__ == '__main__':
    A = np.array([[2, 1], [1.5, 3]])
    b = np.array([-7, 9]).reshape((2, 1))
    u0 = np.array([[0], [0]])
    uz = minimizer(A, b, u0, lr=0.1, max_iter=500, use_line_search=True)
    print('type=', type(uz))
    print('shape=', uz.shape)
    print(':  u*=', uz)
    print(':  loss(u*)=', loss(A, b, uz))
    print(':  grad(u*)=', grad(A, b, uz))
