# def max_profit( stock_prices_yesterday ):

# 	buy_price = stock_prices_yesterday[0]
# 	sell_price = stock_prices_yesterday[1]
# 	best_profit = sell_price - buy_price
# 	i = 0

# 	for price in stock_prices_yesterday:

# 		# skip first two
# 		if i < 1:
# 			i += 1
# 			pass

# 		# update best profit if it's current potential is higher
		
# 		elif price - buy_price > best_profit:
# 			best_profit = price - buy_price
# 			sell_price = price
		
# 		# always want a lower buying price
# 		elif price <= buy_price:
# 			buy_price = price

# 		# update best_profit
# 		# best_profit = sell_price - buy_price

# 	return best_profit

def get_max_profit(stock_prices):
    buy = stock_prices[0]
    sell = stock_prices[1]
    profit = sell - buy
    for x in range(1,len(stock_prices)):
	    
        if stock_prices[x] - buy > profit:
            profit = stock_prices[x] - buy
            sell = stock_prices[x]
        elif stock_prices[x] <= buy:
            buy = stock_prices[x]
    
    return profit


print(max_profit([1,5,3,2]))
print(max_profit([7,2,8,9]))
print(max_profit([1,6,7,9]))
print(max_profit([9,7,4,1]))
print(max_profit([1,1,1,1]))