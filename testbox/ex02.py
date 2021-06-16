import re
mail=input('ここにメールアドレスを入れて')

def mailCheck(mail):
	count = 0
	countAt = 0
	for i in mail:
		# print(i)
		if i=='@':
			countAt+=1
			if count == 0:
				print('何かおかしいです1')
				break
			elif count == len(mail):
				print('何かおかしいです2')
				break


		if countAt == 2:
			print('何かおかしいです3')
			break

		

		count+=1
		
		if count == len(mail):
			print('正しいメールアドレスです')



mailCheck(mail)