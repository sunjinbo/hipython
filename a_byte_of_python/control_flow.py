# 判断语句if
# Python 中不存在 switch 语句
number = 23
guess = int(input('Enter an integer :'))
if guess == number:
    print('You guesssed it.')
elif guess < number:
    print('No, it\'s a little higher than that')
else:
    print('No, it\'s a little lower than that')


# 循环语句
count = 10
while count > 0:
    count -= 1

for i in range(1, 5):
    print(str(i))

value = 10
while True:
    if value > 0:
        continue
    else:
        break


