"""
Problem 2.1 asks for the gradients ∂L/∂ø0 and ∂L/∂ø1 of the loss function:

L(ø0, ø1) = sum((ø0 + ø1xi - yi)^2)

These are

∂L/∂ø0 = 2 * sum(ø0 + ø1xi - yi)
∂L/∂ø1 = 2 * sum((ø0 + ø1xi - yi) * xi)

Problem 2.2 asks to set both to zero and solve for ø0 and ø1:

∂L/∂ø0
2 * sum(ø0 + ø1xi - yi) = 0
sum(ø0 + ø1xi - yi) = 0
sum(ø0) + sum(ø1xi) - sum(yi) = 0
sum(ø0) + sum(ø1xi) = sum(yi)
ø0 * I + sum(ø1xi) = sum(yi)
ø0 * I = sum(yi) - sum(ø1xi)
ø0 = (sum(yi) - ø1 sum(xi)) / I

∂L/∂ø1
2 * sum((ø0 + ø1xi - yi) * xi) = 0
sum((ø0 + ø1xi - yi) * xi) = 0
sum(ø0xi + ø1xi^2 - yixi) = 0
sum(ø0xi) + sum(ø1xi^2) - sum(yixi) = 0
sum(ø0xi) + sum(ø1xi^2) = sum(yixi)
sum(ø1xi^2) = sum(yixi) - sum(ø0xi)
ø1 * sum(xi^2) = sum(yixi) - sum(ø0xi)
ø1 = (sum(yixi) - ø0 sum(xi)) / sum(xi^2)

Now replacing ø0 into ø1:

sum(ø0xi + ø1xi^2 - yixi) = 0
ø0 sum(xi) + ø1sum(xi^2) = sum(yixi)
-- replace ø0 --
((sum(yi) - ø1 sum(xi)) / I) * sum(xi) + ø1sum(xi^2) = sum(yixi)
((sum(yi) sum(xi) - ø1 sum(xi)^2) / I) + ø1sum(xi^2) = sum(yixi)
sum(yi) sum(xi) - ø1 sum(xi)^2 + I ø1 sum(xi^2) = I sum(yixi)
I ø1 sum(xi^2) - ø1 sum(xi)^2 = I sum(yixi) - sum(yi) sum(xi)
ø1 (I sum(xi^2) - sum(xi)^2) = I sum(yixi) - sum(yi) sum(xi)
ø1 = (I sum(yixi) - sum(yi) sum(xi)) / (I sum(xi^2) - sum(xi)^2)

With this last equation we can solve slope and intercept 
for a list of points (x, y)
"""


def solve(points):
    I = len(points)
    sum_xi = sum(x for x, _ in points)
    sum_yi = sum(y for _, y in points)
    sum_xi2 = sum(x**2 for x, _ in points)
    sum_yixi = sum(x * y for x, y in points)
    ø1 = (I * sum_yixi - sum_yi * sum_xi) / (I * sum_xi2 - sum_xi**2)
    ø0 = (sum_yi - sum_xi * ø1) / I
    return ø0, ø1


def solve_generative(points):
    I = len(points)
    sum_xi = sum(x for x, _ in points)
    sum_yi = sum(y for _, y in points)
    sum_yixi = sum(x * y for x, y in points)
    sum_yi2 = sum(y**2 for _, y in points)
    ø1 = (I * sum_yixi - sum_xi * sum_yi) / (I * sum_yi2 - sum_yi**2)
    ø0 = (sum_xi - sum_yi * ø1) / I
    return ø0, ø1


def main():
    book_xs = [0.03, 0.19, 0.34, 0.46, 0.78, 0.81, 1.08, 1.18, 1.39, 1.60, 1.65, 1.90]
    book_ys = [0.67, 0.85, 1.05, 1.0, 1.40, 1.5, 1.3, 1.54, 1.55, 1.68, 1.73, 1.6]
    xs = [2, 3, 5, 8]
    ys = [2.5, 1.9, 6.2, 7.5]
    points = list(zip(xs, ys))
    ø0, ø1 = solve(points)
    gø0, gø1 = solve_generative(points)
    print(f"f[ø, x] -> y ø0 = {ø0:.2f}, ø1 = {ø1:.2f}")
    print(f"g[ø, y] -> x ø0 = {gø0:.2f}, ø1 = {gø1:.2f}")


if __name__ == """__main__""":
    main()
