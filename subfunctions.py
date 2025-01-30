def sum_product(x,y):
        if len(x) == len(y):
            product_list=[]
            for i in range(len(x)):
                element = x[i]*y[i]
                product_list.append(element)
            sum_product_x_y= sum(product_list)
            return sum_product_x_y
    
        else:
            raise Exception('The length of x and y are not the same')