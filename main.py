import medicine_manager
import storage_manager
import reminder_setter
import time

def header(text:str):
    print(purple(text.center(50,"-")))

def red(text):
    return f"\033[91m{text}\033[0m"

def green(text):
    return f"\033[92m{text}\033[0m"

def blue(text):
    return f"\033[96m{text}\033[0m"

def yellow(text):
    return f"\033[93m{text}\033[0m"

def purple(text):
    return f"\033[95m{text}\033[0m"

#Greeting function
def greeting():
    loc_time=int(time.strftime("%H"))

    if 5<=loc_time<12:
        print("GOOD MORNING")
    elif 12<=loc_time<18:
        print("GOOD AFTERNOON")
    else:
        print("GOOD EVENING")

def show_menu():
    print(purple("MENU".center(50,"-")))
    print(yellow("1. Insert Medicine"))
    print(yellow("2. Remove Medicine"))
    print(yellow("3. View Medicine Data"))
    print(yellow("4. Load Medicine Data"))
    print(yellow("5. Save Medicine Data"))
    print(yellow("6. Turn On Reminder"))
    print(yellow("7. Exit"))

def main():
    greeting()
    storage_manager.load_system()
    while True:    

        show_menu()

        try:
            choice=int(input(blue("Enter menu number : ")))
            match choice:
                case 1:
                    header("Medicine Manager")
                    medicine_manager.get_data()
                    print()

                case 2:
                    header("Medicine Manager")
                    medicine_manager.remove_medicine()
                    print()

                case 3:
                    header("Storage Manager")
                    storage_manager.view_data()
                    print()

                case 4:
                    header("Storage Manager")
                    storage_manager.load_system()
                    print(green("System loaded successfully"))
                    print()

                case 5:
                    header("Storage Manager")
                    storage_manager.save_system()
                    print(green("Data saved successfully"))
                    print()

                case 6:
                    reminder_setter.reminder()

                case 7:
                    storage_manager.save_system()
                    print(green("Data saved. Thank You!"))
                    break

                case _:
                    print(red("Choose a number between 1 and 7."))

        except ValueError:
            print(red("Choice must be number!"))
if __name__=="__main__":
    main()