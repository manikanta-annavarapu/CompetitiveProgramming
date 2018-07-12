

def queue_reconstruct(persons):

	final_queue = [persons[0]]*len(persons)
	# print(final_queue)

	for i in range(1,len(persons)):
		# print("yo")
		person = persons[i]

		for j in range(person[1],len(persons)):
			# print("yo")
			# print(final_queue[j][0] , person[0])
			if final_queue[j][0] >= person[0]:
				final_queue[j] = person

	for x in persons:
		if x in final_queue:
			pass
		else:
			for y in range(len(final_queue)):
				if final_queue[y][0] < x[0]:
					final_queue[y+1] = x
					break



	return final_queue			

			

print(queue_reconstruct([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]))