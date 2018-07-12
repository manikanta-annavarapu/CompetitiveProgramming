

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

def unique_morse_code(words):

	morse_list = []
	for word in words:
		temp_str = ""
		for letter in word:
			temp_str += MORSE_CODE_DICT[letter.upper()]
		morse_list.append(temp_str)

	# print(morse_list) 
	refined_list = []

	for x in morse_list:
		if x not in refined_list:
			refined_list.append(x)

	return len(refined_list)


print(unique_morse_code(["gin", "zen", "gig", "msg"]))
print(unique_morse_code(["a", "z", "g", "m"]))
print(unique_morse_code(["bhi", "vsv", "sgh", "vbi"]))
print(unique_morse_code(["a", "b", "c", "d"]))
print(unique_morse_code(["hig", "sip", "pot"]))