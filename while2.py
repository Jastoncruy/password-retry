x = 2
while x >= 0:
	Account = input('请输入账号: ')
	Password = input('请输入密码: ')
	if Password == '123':
		print('成功登陆')
		break
	else:
		if x > 0:
			print('账号或密码错误, 请重新输入,你还有',x,'次机会')
		else:
			print('账号或密码错误, 拒绝访问')
	x = x - 1