numbersList = [13, 17, 31, '', 57, 41, 83]

def remove(list):
	list.pop(3)



def average(list):
	x = 0
	for i in list:
		# print(i)
		x += i
	print(f'平均値：{x/len(list)}')


remove(numbersList)
print(numbersList)
average(numbersList)
