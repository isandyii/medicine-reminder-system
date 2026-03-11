from storage_manager import load_system,medicine_data
import time
from plyer import notification

def green(text):
    return f"\033[92m{text}\033[0m"

def reminder():#reminder
    load_system()
    print(green("Reminder Started".center(50,"-")))
    while True:
        current_time=time.strftime("%I:%M %p")
        for med in medicine_data:    
            if current_time in medicine_data[med]:
                
                print(f"\033[46m{current_time} its time to take {med}!\033[0m")

                notification.notify(
                title="Medicine Reminder",
                message=f"Time to take {med}",
                timeout=10
                )
        time.sleep(60) 