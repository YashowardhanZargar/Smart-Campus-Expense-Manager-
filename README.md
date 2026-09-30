Smart Campus Expense Manager

A Python-based expense management project designed to help students manage, record, and track their campus-related expenses.

Project Overview

Managing daily expenses can be difficult for students, especially when spending is spread across food, travel, stationery, entertainment, academic requirements, and other campus activities.

The Smart Campus Expense Manager provides a simple way to record and manage expenses from the command line. The project is developed using Python and demonstrates fundamental programming concepts such as variables, data types, conditional statements, loops, functions, file/database handling, and user input.

Features

Add and record expenses

View recorded expenses

Organize expenses based on categories

Track spending information

Calculate expense totals

Manage campus-related financial records

Command-line based interaction

Simple and easy-to-use interface

Technology Used

Python 3

Python standard libraries and project dependencies

Local data storage used by the application

Project Structure
Smart-Campus-Expense-Manager-
│
├── README.md
│
└── smart-campus-expense-manager/
    └── Project source files

Requirements

Before running the project, make sure the following software is installed:

Python 3.8 or later

Git

pip (Python package installer)

You can verify your Python installation using:

python --version


or:

python3 --version


Verify pip using:

pip --version

Installation
1. Clone the repository

Open a terminal and run:

git clone https://github.com/YashowardhanZargar/Smart-Campus-Expense-Manager-.git

2. Open the project directory
cd Smart-Campus-Expense-Manager-


Then enter the application directory:

cd smart-campus-expense-manager

3. Create a virtual environment

It is recommended to use a virtual environment.

On Windows:

python -m venv venv


Activate it using:

venv\Scripts\activate


On macOS/Linux:

python3 -m venv venv


Activate it using:

source venv/bin/activate

4. Install dependencies

If the project contains a requirements.txt file, install the required packages using:

pip install -r requirements.txt


If the project does not contain a requirements.txt file, the application can be run using the Python dependencies included in the project.

Configuration

The project is designed to run locally.

If any configuration file, database file, or environment variable is required by the application, make sure it is present in the project directory before starting the application.

Do not commit passwords, API keys, private credentials, or other sensitive information to the repository.

Running the Project

After completing the installation steps, run the project's main Python file from the smart-campus-expense-manager directory.

For example, if the main file is main.py:

python main.py


On systems where Python 3 is accessed using python3:

python3 main.py


Follow the instructions displayed in the terminal to interact with the application.

How to Use

After starting the application:

Follow the menu displayed in the terminal.

Select the required operation.

Enter the requested expense information.

Save or submit the expense when prompted.

Use the available options to view or manage recorded expenses.

Exit the application using the provided exit option.

Example Use Case

A student purchases lunch for ₹120.

The student can enter the expense through the application and provide information such as:

Amount: 120
Category: Food
Description: Lunch


The application can then store the expense and include it in the student's expense records and total spending.

Error Handling

The application is intended to handle normal user input and prevent invalid values from causing unexpected termination wherever validation is implemented.

If an error occurs:

Check that Python is installed correctly.

Make sure you are running the program from the correct directory.

Verify that required dependencies have been installed.

Check that required project/data files are present.

Read the error message shown in the terminal for troubleshooting information.

Project Objective

The objective of this project is to apply Python programming concepts to a practical campus-related problem. The application provides a simple expense management solution while demonstrating programming fundamentals learned in the Python Essentials course.

Course

Course: Python Essentials

Project: Smart Campus Expense Manager

Author

Yashowardhan Zargar

GitHub Repository:

https://github.com/YashowardhanZargar/Smart-Campus-Expense-Manager-

License

This project was developed as part of the Python Essentials course evaluation.
