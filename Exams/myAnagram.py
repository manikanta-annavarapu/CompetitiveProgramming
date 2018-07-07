# str1 = str(input())
# str2 = str(input())




def myanagram(str1,str2):
	str1 = "".join(str1.lower().split())
	str2 = "".join(str2.lower().split())
	# print(str1)
	for x in str2:
		if x in str1:
			pass
		else:
			return False
	return True

# print(myanagram("anagram","nagaram"))
print("myanagram(\"anagram\",\"nagaram\") = ", myanagram("anagram","nagaram"))
print("myanagram(\"Keep\",\"Peek\") = ",myanagram("Keep","Peek"))
print('myanagram("Mother In Law","Hitler Woman") = ',myanagram("Mother In Law","Hitler Woman"))
print('myanagram("School Master","Ther Classroom") = ',myanagram("School Master","Ther Classroom"))
print('myanagram("ASTRONOMERS","NO MORE STARS") =',myanagram("ASTRONOMERS","NO MORE STARS"))
print('myanagram("Toss","Shot") = ',myanagram("Toss","Shot"))
print('myanagram("joy","enjoy") = ',myanagram("joy","enjoy"))
print('myanagram("Debit Card","Bad Credit") = ',myanagram("Debit Card","Bad Credit"))
print('myanagram("SiLeNt CAT","LisTen AcT") =- ',myanagram("SiLeNt CAT","LisTen AcT"))
print('myanagram("Dormitory","Dirty Room") = ',myanagram("Dormitory","Dirty Room"))