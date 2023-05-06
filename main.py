import math

#Simple Iterative Method
def g(x):
    return math.cos(x)
x0 = 0.5
tolerance = 1e-6
while abs(g(x0) - x0) > tolerance:
    x0 = g(x0)
print("The root of the equation is approximately:", x0)

#bisection Method
def f(x):
    return x - math.cos(x)
def bisection(a, b, tol=1e-6, max_iter=1000):
    if f(a) * f(b) > 0:
        raise ValueError("Function has same signs at a and b")
    for i in range(max_iter):
        c = (a + b) / 2
        fc = f(c)
        if abs(fc) < tol:
            return c
        if f(a) * fc < 0:
            b = c
        else:
            a = c
    raise ValueError("Method did not converge within max_iter iterations.")
solution = bisection(0, 1)
print("The solution using bisection method is:", solution)

#NEWTON RAPHSON METHOD
def f(x):
    return x - math.cos(x)
def f_prime(x):
    return 1 + math.sin(x)
def newton_raphson(x0, tol=1e-6, max_iter=1000):
    x = x0
    for i in range(max_iter):
        fx = f(x)
        if abs(fx) < tol:
            return x
        fpx = f_prime(x)
        if fpx == 0:
            raise ValueError("Derivative is zero")
        x = x - fx / fpx
    raise ValueError("Method did not converge within max_iter iterations.")
solution = newton_raphson(1)
print("The solution using newton raphson method  is:", solution)

# Secant method
def f(x):
    return x - math.cos(x)
def secant(x0, x1, tol=1e-6, max_iter=1000):
    for i in range(max_iter):
        x_next = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        if abs(x_next - x1) < tol:
            return x_next
        x0, x1 = x1, x_next
solution = secant(0, 1)
print("The solution is using secant method:", solution)
