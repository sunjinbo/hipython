import os
import sys

def print_with_format(var, fn=sys.stdout):
    if isinstance(var, list):
        for v in var:
            print(v, file=fn)
    elif isinstance(var, str):
        print("#" + var, file=fn)
    else:
        print('We can not recognize var!', file=fn)

jerry = []
fei = []

try:
    data = open('sketch.txt')

    try:
        for each_line in data:
            (role, spoken_line) = each_line.split(':')
            if role == 'Jerry':
                jerry.append(spoken_line)
            elif role == 'Fei':
                fei.append(spoken_line)
    except ValueError:
        pass

    data.close()
except IOError:
    print("The data file is missing.")

print(jerry)
print(fei)

try:
    jerry_output = open('jerry_output.txt', 'w')
    fei_output = open('fei_output.txt', 'w')

    print_with_format(jerry, jerry_output)
    print_with_format(fei, fei_output)

    with open('with_test.txt', 'w') as with_test_output:
        print_with_format('Test with sentence!', with_test_output) 

except IOError as err:
    print('Fille error: ' + str(err))

finally:
    if 'jerry_output' in locals():
        jerry_output.close()
    if 'fei_output' in locals():
        fei_output.close()    
