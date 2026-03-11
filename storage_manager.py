import json

def red(text):
    return f"\033[91m{text}\033[0m"

medicine_data={}

def save_system():
    with open("Medicine_data_file.json","w") as f1:
        json.dump(medicine_data,f1,indent=4)

def load_system():
    try:
        with open("Medicine_data_file.json","r") as f2:
            f2_data=json.load(f2)
            medicine_data.update(f2_data)
    except FileNotFoundError:
        print(red("File NOT FOUND!"))
        return {}
    except json.JSONDecodeError:
        print(red("File is empty!"))
        return {}
    
def view_data():
    try:
        with open("Medicine_data_file.json","r") as f3:
            print(json.load(f3))
    except FileNotFoundError:
        print(red("File Not found"))
    except json.JSONDecodeError:
        print(red("File is empty"))
