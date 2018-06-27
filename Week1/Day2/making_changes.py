def change_possibilities(amount, denominations):

    arr = [0]*(amount+1)
    arr[0] = 1

    for i in range(len(denominations)):
    	for j in range(len(arr)):
    		if j>= denominations[i]:
    			arr[j] = arr[j]+arr[j-denominations[i]]
    

    return arr[len(arr)-1]

print(change_possibilities(4, (1, 2, 3)))
print(change_possibilities(0, (1, 2)))
print(change_possibilities(1, ()))
print(change_possibilities(5, (25, 50)))
print(change_possibilities(100, (1, 5, 10, 25, 50)))