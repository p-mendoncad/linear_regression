#add correlation and coefficient of determination
import matplotlib.pyplot as plt
from subfunctions import *
class LinReg:

    def __init__(self, x: list, y: list):
        if not x or not y:
            raise AttributeError('One or both lists are empty')
        elif any(i is None for i in x) or any(i is None for i in y):
            raise ValueError("One or both lists contain None elements")
        elif len(x) != len(y):
            raise AttributeError('The length of x and y are not the same')
        else:
            self.x = x
            self.y = y

    def get_n(self):
        return len(self.x)

    def sum_product_x_y(self):
        result = sum(x_i * y_i for x_i, y_i in zip(self.x, self.y))
        return result

    def sum_x(self):
        result = sum(self.x)
        return result

    def sum_y(self):
        result = sum(self.y)
        return result

    def sum_x_squared(self):
        result = sum(num ** 2 for num in self.x)
        return result

    def square_sum_x(self):
        result = self.sum_x() ** 2
        return result

    def get_m(self):
        numerator = (self.get_n() * self.sum_product_x_y()) - (self.sum_x() * self.sum_y())
        denominator = (self.get_n() * self.sum_x_squared()) - self.square_sum_x()
        if denominator == 0:
            raise ZeroDivisionError("Denominator is zero, cannot calculate slope.")
        m = numerator / denominator
        return m

    def get_b(self):
        b = mean(self.y) - (self.get_m() * mean(self.x))
        return b

    def get_equation(self):
        m = self.get_m()
        b = self.get_b()
        equation = f'f(x) = {round(m, 5)}x + ({round(b, 5)})'
        return equation
    
    def metrics(self):
        residuals = [self.y[i] - (self.get_m() * self.x[i] + self.get_b()) for i in range(self.get_n())]
        residuals = [round(r, 5) for r in residuals]
        ssr = sum([i**2 for i in residuals])
        mse = ssr/self.get_n()
        info = f'\n{residuals} \nSSR: {ssr}\nMSE: {mse}'
        return info


    def plot(self):
        x_range = [min(self.x), max(self.x)]
        y_range = [self.get_m() * x_i + self.get_b() for x_i in x_range]

        plt.scatter(self.x, self.y, color='red', label='Data points')

        plt.plot(x_range, y_range, color='blue', linestyle='-', label='Regression line')

        plt.axhline(0, color='black', linewidth=0.5)
        plt.axvline(0, color='black', linewidth=0.5)
        plt.xlabel("x")
        plt.ylabel("y")
        plt.title(f"Linear Regression Equation: {self.get_equation()}")
        plt.legend()
        plt.grid(True, linestyle="--", alpha=0.6)

        plt.show()