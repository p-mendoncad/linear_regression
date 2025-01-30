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
    print(equation)
    # print(sum_x)
    # print(sum_x_squared)
    # print(sum_product_x_y)
    # print(sum_y)
    # print(square_sum_x)
                                         
linear_regression_equation([1,2,3,4,5,6,7],[1,1.2,1,2,3,2.6,3.4])