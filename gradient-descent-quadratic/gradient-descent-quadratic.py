def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    for _ in range(steps):
        output = a*x0**2 + b*x0 + c
        grad = 2*a*x0 + b
        x0 = x0 - lr * grad
    return x0