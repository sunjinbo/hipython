# 异常处理
class ShortInputException(Exception):
    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast


try:
    with open('poem.txt') as f:
        for line in f:
            print(line, end='')
    text = input("Enter something:")
    if len(text) < 3:
        raise ShortInputException(len(text), 3)
except EOFError:
    print("Why did you do an EOF on me?")
except KeyboardInterrupt:
    print("You cancelled the operation.")
except FileNotFoundError:
    print("No such file or directory.")
except ShortInputException as ex:
    print(('The input was {0}, at least {1}').format(ex.length, ex.atleast))
else:
    print('You entered {}'.format(text))
finally:
    print("-END-")

