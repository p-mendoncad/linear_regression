import matplotlib.pyplot as plt
from subfunctions import *

def linear_regression_equation(x,y):
    sum_product_x_y=sum_product(x,y)
    sum_x = sum(x)
    sum_y = sum(y)
    sum_x_squared =sum(n**2 for n in x)
    square_sum_x = sum_x**2

# y = mx + b
# n = len(x) = len(y)
    n = len(x)
    m = (n * sum_product_x_y - sum_x * sum_y) / ((n * sum_x_squared) - square_sum_x)
    b = mean(y) - (m * mean(x))
  
    equation = f'f(x) = {round(m, 5)}x + ({round(b,5)})'
    
    x_range = [min(x), max(x)]
    y_range = [m * x_i + b for x_i in x_range]

    residuals = [y[i] - (m * x[i] + b) for i in range(n)]
    ssr = sum([i**2 for i in residuals])
    mse = ssr/n

    print(f'{equation} \n{residuals} \nSSR: {ssr}\nMSE: {mse}')

    plt.scatter(x, y, color='red', label='Data points')

    plt.plot(x_range, y_range, color='blue', linestyle='-', label='Regression line')

    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title(f"Linear Regression Equation: {equation}")
    plt.legend()
    plt.grid(True, linestyle="--", alpha=0.6)

    plt.show()