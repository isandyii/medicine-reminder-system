# Medicine Reminder System

## Description

The **Medicine Reminder System** is a command-line Python application that helps users manage and track their medicine schedules efficiently.

This application allows users to add medicines with specific reminder times, store the data using **JSON for persistent storage**, and receive **desktop notifications** when it is time to take their medicine.

The project is designed using a **modular architecture**, where different functionalities such as medicine management, data storage, and reminder notifications are handled by separate modules.

---

## Features

* Add medicines with reminder time
* Remove medicines from the system
* View stored medicine schedules
* Save and load medicine data using JSON
* Automatic time-based reminder system
* Desktop notifications using Plyer
* Menu-driven command line interface

---

## Technologies Used

* Python
* JSON (for data storage)
* Time module
* Plyer (for desktop notifications)
* Modular programming

---

## Project Structure

```
medicine-reminder-system/
│
├── main.py
├── medicine_manager.py
├── storage_manager.py
├── reminder_setter.py
│
├── Medicine_data_file.json
│
└── README.md
```

---

## How to Run the Project

1. Clone the repository

```
git clone https://github.com/your-username/medicine-reminder-system.git
```

2. Navigate to the project folder

```
cd medicine-reminder-system
```

3. Install required dependency

```
pip install plyer
```

4. Run the program

```
python main.py
```

---

## Future Improvements

This project will continue to be improved with additional features such as:

* Improved user interface
* More advanced reminder options
* Possible GUI version using Python libraries
* Additional medicine management features

---

## Author

Developed as a Python learning project to practice modular programming, file handling, and automation.
