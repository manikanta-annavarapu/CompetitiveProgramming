
def keysAndRoom(rooms):

	length = len(rooms) 
	dic = {}
	for x in range(length):
		dic[x] = False
	# print(dic)
	dic[0] = True
	TrueCount = 1
	# print(dic)

	for x in range(length):
		if(dic[x]):
			# print("yo = ",rooms[x])
			for keys in rooms[x]:
				if keys < length and dic[keys] == False:
					dic[keys] = True
					TrueCount+=1

		else:
			break
	# print(TrueCount)
	if TrueCount == length:
		return True
	else:
		return False


print(keysAndRoom([[1], [0,2], [3]]))
print(keysAndRoom([[1,3], [3,0,1], [2], [0]]))
print(keysAndRoom([[1,2,3], [0], [0], [0]]))
print(keysAndRoom([[1], [0,2,4], [1,3,4], [2], [1,2]]))
print(keysAndRoom([[1], [2,3], [1,2], [4], [1], [5]]))
print(keysAndRoom([[1], [2], [3], [4], [2]]))
print(keysAndRoom([[1], [1,3], [2], [2,4,6], [], [1,2,3], [1]]))

