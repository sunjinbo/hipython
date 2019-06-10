import pickle
import io


def reverse(text):
    return text[::-1]


def is_palindrome(text):
    aar = [' ', ',', '.', '!', '?']
    for i in range(len(aar)):
        text = text.replace(aar[i], '')
    text = text.casefold()
    return text == reverse(text)


something = input("Enter text: ")
if is_palindrome(something):
    print("Yes, it is a palindrome")
else:
    print("No, it is not a palindrome")


palindrome_text = "Rise to vote, sir."
print(palindrome_text)
if is_palindrome(palindrome_text):
    print("Yes, it is a palindrome")
else:
    print("No, it is not a palindrome")


poem = '''\n
    Programming is fun
    When the work is done
    if you wanna make your work also fun:
        use Python！
    '''


f = open('poem.txt', 'w')
f.write(poem)
f.close()


f = open('poem.txt', 'r')
while True:
    line = f.readline()
    if len(line) == 0:
        break
    print(line, end='')
f.close()


# Pickle标准模块
shop_list_file = "shoplist.dat"
shop_list = ['apple', 'mango', 'carrot']

f = open(shop_list_file, 'wb')
pickle.dump(shop_list, f)
f.close()

del shop_list

f = open(shop_list_file, 'rb')
stored_list = pickle.load(f)
print(stored_list)


# Unicode
f = io.open('abc.txt', 'w', encoding="utf-8")
f.write(u"我爱你中国")
f.close()

text = io.open('abc.txt', encoding="utf-8").read()
print(text)

