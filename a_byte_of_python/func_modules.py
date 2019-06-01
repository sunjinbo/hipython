from math import sqrt
import sys


# 函数
def say_hello():
    print("hello, world!")


say_hello()
say_hello()


def print_max(a, b):
    if a > b:
        print(a, 'is maximum')
    elif a == b:
        print(a, 'is equal to', b)
    else:
        print(b, 'is maximum')


print_max(3, 4)
print_max(4, 4)


x = 50
y = 40


def func(x):
    global y
    print('x is', x)
    print('y is', y)
    x = 30
    y = 20


func(x)
func(y)
print('global x is', x)
print('global y is', y)


def say(meessage, times=1):
    print(meessage * times)


say('hello')
say('world', 3)


def func(a, b=5, c=10):
    print('a is', a, 'and b is', b, 'and c is', c)


func(3, 7)
func(25, c=24)
func(c=50, a=100)


# 声明一个诸如 *param 的星号参数时，从此处开始直到结束的所有位置参数
# （Positional Arguments）都将被收集并汇集成一个称为“param”的元组（Tuple）。
def func(*params):
    # 遍历元组中的所有项目
    for item in params:
        print('item', item)


# 声明一个诸如 **param 的双星号参数时，从此处开始直至结束的所有关键字
# 参数都将被收集并汇集成一个名为 param 的字典（Dictionary）
def func(**params):
    # 遍历字典中的所有项目
    for first_part, second_part in params.items():
        print(first_part, second_part)


def none_func():
    pass


# 模块
print("Square root of 16 is", sqrt(16))
print('__name__ is', __name__)

if __name__ == '__main__':
    print('This program is being run by itself')
else:
    print('I am being imported from another module')


dir(sys)
dir()

