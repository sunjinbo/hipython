# 单行注释


# 字符串之单引号和双引号
print('I\'m a student')
print("I'm a student")
print("Jason said \"I like you\"")
print('Jason said "I like you"')


# 字符串之三引号"""或'''
print('''This is the second line.
"What's your name?," I asked.
He said "Bond, James Bond."
''')


# 字符串之格式化
age = 20
name = 'Swaroop'
print('{0} was {1} years old when he wrote this book'.format(name, age))
print('{} was {} years old when he wrote this book'.format(name, age))
print('{name} wrote {book}'.format(name='Swaroop', book='A Byte of Python'))


# 字符串之原始字符串
print(r"Newlines are indicated by \n")


# 防止打印过程中出现换行符
print('a', end='')
print('b', end='')
