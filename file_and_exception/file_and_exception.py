import os

print(os.getcwd())

data = open('sketch.txt')

print(data.readline())
print(data.readline())
print(data.readline())
print(data.readline())

data.seek(0)

for each_line in data:
    (role,line_spoken) = each_line.split(":")
    print(role);print(" said: ");print(line_spoken)

data.close()

