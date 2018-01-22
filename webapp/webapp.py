import pickle
from objects import Athlete
from objects import get_coach_data

def put_to_store(files_list):
    all_athletes = {}
    for each_file in files_list:
        ath = get_coach_data(each_file)
        all_athletes[ath.name]=ath

    try:
        with open("athletes.pickle", "wb") as athf:
            pickle.dump(all_athletes, athf)
    except IOError as err:
        print("File Error:" + str(err))
    
    return all_athletes

def get_from_store():
    all_athletes = {}
    try:
        with open("athletes.pickle", "rb") as athf:
            all_athletes = pickle.load(athf)
    except IOError as err:
        print("File Error:" + str(err))
    
    return all_athletes

files_list = {"james2.txt", "julie2.txt", "mikey2.txt", "sarah2.txt"}
all_athletes = put_to_store(files_list)
all_athletes = get_from_store()
