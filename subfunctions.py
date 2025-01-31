def sum_product(x,y):
    if not x or not y:
        raise ValueError('One or both lists are empty')
    if any(i is None for i in x) or any(i is None for i in y):
        raise ValueError("One or both lists contain None elements")
    if len(x)!=len(y):
        raise ValueError('The length of x and y are not the same')
    else:
        product_list=[]
        for i in range(len(x)):
            element = x[i]*y[i]
            product_list.append(element)
            sum_product_x_y= sum(product_list)
        return sum_product_x_y
    

def mean(list):
     mean = sum(list)/len(list)
     return mean