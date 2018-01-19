import os

def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return time_string

    (mins,secs)=time_string.split(splitter)
    return mins + '.' + secs;

def parse_file(file_name):
    with open(file_name) as file:
        file_line = file.readline()
        data = file_line.strip().split(',')

        clean_data = []
        for each_d in data:
            unique_d = sanitize(each_d)
            if unique_d not in clean_data:
                clean_data.append(unique_d)

        #clean_data=[sanitize(each_d) for each_d in data]
        
        print("#" + file_name)
        print("orignal:" + str(clean_data))
        sorted_data = sorted(clean_data)
        print("sorted:" + str(sorted_data[0:3]))
        clean_data.sort()
        print("sort:" + str(clean_data[0:3]))

try:
    parse_file('james.txt')
    parse_file('julie.txt')
    parse_file('mikey.txt')
    parse_file('sarah.txt')

except IOError as err:
    print("File error:" + str(err))

