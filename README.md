# Medicine Reminder System

The Medicine Reminder System is a command-line Python application that helps users manage and track their medicine schedules efficiently.

This application allows users to add medicines with specific reminder times, store the data using JSON for persistent storage, and receive desktop notifications when it is time to take their medicine.

The project is designed using a modular architecture with separate modules for medicine management, data storage, and the reminder system.

## Features

* Add medicines with reminder time
* Remove medicines from the system
* View stored medicine schedules
* Save and load medicine data using JSON
* Automatic time-based reminder system
* Desktop notifications using Plyer
* Menu-driven command line interface

## Technologies Used

* Python
* JSON
* Time module
* Plyer (for desktop notifications)
* Modular programming

## Project Structure

medicine-reminder/
│
├── main.py                  # Main program entry point and menu system
├── medicine_manager.py      # Handles adding and removing medicines
├── storage_manager.py       # Handles saving and loading medicine data
├── reminder_setter.py       # Runs the reminder system and notifications
│
├── Medicine_data_file.json  # JSON file used to store medicine schedules
│
└── README.md                # Project documentation

## Future Improvements

This project will continue to be improved with additional features such as better user interface, more advanced reminder options, and possible GUI implementation.
