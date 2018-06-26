from functools import reduce


def get_products_of_all_ints_except_at_index(int_list):

    # Make a list with the products
    if len(int_list)<2:
        raise IndexError("Getting the product of numbers at other indices requires at least 2 numbers")
    
    res = []
    temp = [None]*len(int_list)
    product = 1
    for i in range(len(int_list)):
        res.append(product)
        product *= int_list[i]
    # print(res)
    product = 1
    for i in range(len(int_list)-1,-1,-1):
    	temp[i] = product
    	product *= int_list[i]
    	res[i] *= temp[i]
    # print(res)
        

    return res

print(get_products_of_all_ints_except_at_index([2, 3,4,5,6]))
print(get_products_of_all_ints_except_at_index([8, 2, 4, 3, 1, 5]))
print(get_products_of_all_ints_except_at_index([6, 2, 0, 3]))
print(get_products_of_all_ints_except_at_index([4, 0, 9, 1, 0]))
print(get_products_of_all_ints_except_at_index([-7, -1, -4, -2]))
print(get_products_of_all_ints_except_at_index([]))