from functools import reduce


def get_products_of_all_ints_except_at_index(int_list):

    # Make a list with the products
    res = []
    temp = 1
    product = 1
    for i in range(len(int_list)):
        res.append(product)
        product *= int_list[i]
    print(res)
    product = 1
    for i in range(len(int_list)-1,-1,-1):
    	temp = product
    	product *= int_list[i]
    	res[i] *= temp
    print(res)
        

    return res

print(get_products_of_all_ints_except_at_index([2, 3,4,5,6]))