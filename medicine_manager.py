import json
from storage_manager import medicine_data

def red(text):
    return f"\033[91m{text}\033[0m"

def green(text):
    return f"\033[92m{text}\033[0m"

def get_data():
    while True:
        med = input("Enter the medicine name: ").strip().title()
        if not med:    
            print(red("Medicine name cannot be empty!"))
            continue
        break
    while True:
        try:
            hours = int(input("Set Hours (1-12): "))
            if not (1 <= hours <= 12):
                print(red("Hours must be between 1 and 12!"))
                continue

            minutes = int(input("Set Minutes (0-59): "))
            if not (0 <= minutes <= 59):
                print(red("Minutes must be between 0 and 59!"))
                continue

            am_pm = input("AM / PM: ").strip().upper()
            if am_pm not in ["AM", "PM"]:
                print("Enter only AM or PM!")
                continue

            time_formatted = f"{hours:02}:{minutes:02} {am_pm}"

            if med in medicine_data:
                medicine_data[med].append(time_formatted)
            else:
                medicine_data[med] = [time_formatted]
            print(green("Medicine added successfully!"))
            break

        except ValueError:
            print(red("Hours and minutes must be numbers!"))

def remove_medicine():
    remove_med=input("Enter which medicine you want to remove.\n").title().strip()
    with open("Medicine_data_file.json","r") as f4:
        try:
            f4_data=json.load(f4)
            if remove_med in f4_data:
                while True:
                    yes_or_no=input((f"{remove_med} avilable in medicine data do you want to remove ! y/n \n")).strip().upper()
                    if yes_or_no=="Y":
                        medicine_data.update(f4_data)
                        del medicine_data[remove_med]
                        with open("Medicine_data_file.json","w") as f5:
                            json.dump(medicine_data,f5,indent=4)
                            medicine_data.clear()
                        print(red(f"{remove_med} medicine removed and {green("update")}!"))
                        break
                    elif yes_or_no =="N":
                        print(red("operation canceled!"))
                        break                           
            else:
                print(red(f"{remove_med} not found in data!"))
                 
        except json.JSONDecodeError:
            print(red(f" No data available !"))
