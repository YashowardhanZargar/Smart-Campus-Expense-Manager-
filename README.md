Smart Campus Expense Manager






📌 Project Overview

Smart Campus Expense Manager is a Python-based command-line application designed to help students record, organize, and manage their daily campus-related expenses.

The project provides a simple and practical way to maintain expense records and monitor spending. It applies fundamental Python programming concepts to solve a real-world student expense-management problem.

🎯 Project Objectives

The main objectives of this project are:

To provide a simple system for recording student expenses.

To organize expenses according to different categories.

To help users monitor their spending.

To calculate and review total expenses.

To apply Python programming concepts to a practical problem.

To develop a project that can be executed directly from the command line.

✨ Features
Feature	Description
Add Expense	Allows the user to record a new expense.
Expense Categories	Expenses can be organized into relevant categories.
View Expenses	Allows users to view previously recorded expenses.
Expense Tracking	Helps users keep track of their spending.
Total Calculation	Calculates the total amount spent.
Data Management	Maintains expense-related information for later use.
CLI Interface	The application can be operated directly from a terminal.
User Input	Accepts expense information directly from the user.
🛠️ Technologies Used
Technology	Purpose
Python 3	Main programming language
Python Standard Library	Core application functionality
Local Data Storage	Storing expense-related information
Command Line	User interaction and application execution
Git & GitHub	Version control and project hosting
📂 Project Structure
Smart-Campus-Expense-Manager-
│
├── README.md
│
└── smart-campus-expense-manager/
    │
    ├── Project source files
    ├── Python files
    └── Other required project files


The main application files are located inside the smart-campus-expense-manager directory.

💻 System Requirements
Requirement	Version / Details
Operating System	Windows / macOS / Linux
Python	3.8 or later
Git	Required for cloning the repository
pip	Python package installer
Internet	Required during initial installation if external packages are used

Check your Python version:

python --version


If your system uses python3:

python3 --version


Check pip:

pip --version

🚀 Installation & Setup
1. Clone the Repository

Open a terminal or command prompt and run:

git clone https://github.com/YashowardhanZargar/Smart-Campus-Expense-Manager-.git

2. Enter the Repository
cd Smart-Campus-Expense-Manager-

3. Enter the Application Directory
cd smart-campus-expense-manager

4. Create a Virtual Environment

Using a virtual environment is recommended for running the project safely and keeping dependencies isolated.

Windows
python -m venv venv


Activate the environment:

venv\Scripts\activate

macOS / Linux
python3 -m venv venv


Activate the environment:

source venv/bin/activate

📦 Installing Dependencies

If the project contains a requirements.txt file, install the dependencies with:

pip install -r requirements.txt


If the project does not require external Python packages, no additional dependency installation is necessary.

To check installed packages:

pip list

⚙️ Configuration

The application is designed to run locally.

Before running the project:

Make sure Python is installed.

Make sure the project has been cloned correctly.

Enter the smart-campus-expense-manager directory.

Activate the virtual environment if one is being used.

Install the dependencies if a requirements.txt file is provided.

Make sure all required project files are present.

Security

Do not store sensitive information such as:

Passwords

API keys

Personal credentials

Authentication tokens

inside the GitHub repository.

▶️ Running the Application

After completing the setup, run the main Python file from the project directory.

If the main application file is named main.py:

python main.py


For systems using python3:

python3 main.py


The application will start in the terminal and display the available options.

Note: If the project's main Python file has a different filename, run that file instead of main.py.

📖 How to Use

Once the application starts:

Read the menu displayed in the terminal.

Select the required operation.

Enter the requested expense information.

Enter the expense amount.

Select or enter the appropriate category.

Add a description when required.

Save the expense.

View recorded expenses when required.

Use the available options to calculate or review total spending.

Exit the application using the provided exit option.

💰 Example Expense

A student purchases lunch for ₹120.

The expense information may look like:

Amount: 120
Category: Food
Description: Lunch


The application records the information and can use it when displaying expense records and calculating total spending.

🧩 Python Concepts Used

The project demonstrates several Python programming concepts:

Python Concept	Application
Variables	Storing expense information
Data Types	Handling amounts, strings, and other values
Input	Accepting information from the user
Conditional Statements	Controlling application decisions
Loops	Repeating menu and user interactions
Functions	Organizing application functionality
Lists / Data Structures	Managing expense information
File/Data Handling	Maintaining expense records
Exception Handling	Managing invalid or unexpected input
Modules	Organizing Python functionality
🔄 Application Workflow
        ┌─────────────────────┐
        │   Start Application │
        └──────────┬──────────┘
                   │
                   ▼
        ┌─────────────────────┐
        │   Display Main Menu │
        └──────────┬──────────┘
                   │
          ┌────────┴────────┐
          ▼                 ▼
   Add Expense        View Expenses
          │                 │
          ▼                 ▼
   Enter Details       Display Records
          │                 │
          └────────┬────────┘
                   │
                   ▼
        ┌─────────────────────┐
        │ Calculate / Review  │
        │     Expenses        │
        └──────────┬──────────┘
                   │
                   ▼
        ┌─────────────────────┐
        │        Exit         │
        └─────────────────────┘

🛠️ Troubleshooting
Python is not recognized

If you receive an error stating that Python is not recognized, install Python and make sure it is added to the system PATH.

Check again with:

python --version

Module Not Found Error

If Python reports that a module is missing and the project contains requirements.txt, run:

pip install -r requirements.txt


Then try running the application again.

Program Does Not Start

Make sure you are inside the correct directory:

cd Smart-Campus-Expense-Manager-
cd smart-campus-expense-manager


Then run the application's main Python file.

Virtual Environment Problems

If you are using a virtual environment, activate it before running the application.

Windows
venv\Scripts\activate

macOS / Linux
source venv/bin/activate

📊 Project Information
Information	Details
Project Name	Smart Campus Expense Manager
Course	Python Essentials
Project Domain	Python / Expense Management
Application Type	Command-Line Application
Programming Language	Python
Repository	GitHub
Author	Yashowardhan Zargar
🎓 Course Information

Course: Python Essentials

Project: Smart Campus Expense Manager

Purpose: Flipped Course Evaluation Project

👨‍💻 Author

Yashowardhan Zargar

GitHub Repository:

https://github.com/YashowardhanZargar/Smart-Campus-Expense-Manager-

📄 License

This project was developed as part of the Python Essentials course evaluation.

✅ Conclusion

The Smart Campus Expense Manager provides a simple approach to recording and managing student expenses through a command-line interface.

The project demonstrates the practical application of Python programming fundamentals, including variables, data types, conditional statements, loops, functions, data handling, and user interaction.

The application can be further extended in the future with features such as graphical interfaces, advanced reports, database integration, monthly spending analysis, budget alerts, and visualization of expense patterns.