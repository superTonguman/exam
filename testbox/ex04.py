ID = input('IDを入力してください：')
password = input('パスワードを入力してください：')

def chackid(id, pas):
	answerid = 'yosino'
	answerpas = 'yt1974'

	if answerid == id and answerpas == pas:
		print('ok')
	else:
		print('no')
chackid(ID, password)