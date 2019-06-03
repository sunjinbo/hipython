# 序列（Sequence）之列表（List）
shoplist = ['apple', 'mango', 'carrot', 'banana']
shoplist.append('orange')
shoplist.sort()
del shoplist[0]
for item in shoplist:
    print(item, end=' ')
print(len(shoplist))


# 序列（Sequence）之元组（Tuple）
# tuple和list非常类似，但是tuple一旦初始化就不能修改
rgb = ('red', 'green', 'blue')
print(rgb)
print(rgb[-1])


# 序列（Sequence）之字典（Dictionary）
ab = {
    'Swaroop': 'swaroop@swaroopch.com',
    'Larry': 'larry@google.com',
    'Matsumoto': 'matz@ruby-lang.org',
    'Spammer': 'spammer@hotmail.com'
}

print("Swaroop's address is", ab['Swaroop'])

del ab['Swaroop']

for name, address in ab.items():
    print('Contact {} at {}'.format(name, address))

if 'Larry' in ab:
    print("Larry's address is", ab['Larry'])


# 无序集合（Collection）之集合（Set）
bri = set(['brazil', 'russia', 'india'])
bricopy = bri.copy()
bricopy.add('china')
bricopy.issuperset(bri)
