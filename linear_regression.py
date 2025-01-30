import pandas as pd
import numpy as np

def sum_product(x,y):
        if len(x) == len(y):
            product_list=[]
            for i in range(len(x)):
                element = x[i]*y[i]
                product_list.append(element)
            sum_product_x_y= sum(product_list)
        else:
            raise Exception('The length of x and y are not the same')

def linear_regression_equation(x,y):
    sum_product_x_y=sum_product(x,y)
    print(sum_product_x_y)
  

    #sum_x=

    #sum_y=

    #sum_x_squared=

    #square_sum_x= sum_x**2
linear_regression_equation([0,2],[1,5])