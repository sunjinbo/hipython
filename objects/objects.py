import os

class Athlete(list):
    def __init__(self,a_name,a_birthday=None,a_times=[]):
        # The code to initialize a "Athlete" object.
        list.__init__([])
        self.name=a_name
        self.birthday=a_birthday
        self.extend(a_times)

    def top3(self):
        return (sorted(set([sanitize(t) for t in self])))[0:3]

def sanitize(time_string):
    if '-' in time_string:
        splitter='-'
    elif ':' in time_string:
        splitter=':'
    else:
        return time_string

    (mins,secs)=time_string.split(splitter)
    return mins+'.'+secs

def get_coach_data(file_name_string):
    try:
        with open(file_name_string) as f:
            data=f.readline()
        raw_data=data.strip().split(',')

        """
        athlete={}
        athlete['Name']=raw_data.pop(0)
        athlete['birthday']=raw_data.pop(0)
        unique_data=[]
        for each_d in raw_data:
            clean_d=sanitize(each_d)
            if clean_d not in unique_data:
                unique_data.append(clean_d)
        athlete['Times']=sorted(unique_data)
        
        print(athlete['Name']+"'s fastest times are:"+str(athlete['Times'][0:3]))
        """

        athlete=Athlete(raw_data.pop(0),raw_data.pop(0),raw_data)
        print(athlete.name+"'s fastest times are:"+str(athlete.top3()))
        
    except IOError as err:
        print("File error:" + str(err))

get_coach_data('james2.txt')
get_coach_data('julie2.txt')
get_coach_data('mikey2.txt')
get_coach_data('sarah2.txt')
