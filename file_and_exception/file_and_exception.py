import os

print(os.getcwd())

try:
    data = open('sketch.txt')

    print(data.readline())
    print(data.readline())
    print(data.readline())
    print(data.readline())

    data.seek(0)

    for each_line in data:
        try:
            if not each_line.find(':') == -1:
                (role,line_spoken) = each_line.split(":")
                print(role);print(" said: ");print(line_spoken)
        except ValueError:
            pass

    data.close()
except IOError:
    print('The data file is missing!')
    
