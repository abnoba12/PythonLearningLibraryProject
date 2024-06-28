# Lesson 1: Introduction to Python and Project Setup

## Objective
The objective of this lesson is to introduce students to Python programming and set up the project structure for the Personal Library Management System. By the end of this lesson, students will have a clear understanding of the project structure and how to run a basic Python script.

## Key Points

1. **Introduction to Python**
   - Brief overview of Python programming language.
   - Benefits of using Python for development.
   - Installation and setup of Python environment (if not already installed).

2. **Setting Up the Project Structure**
   - Importance of an organized project structure.
   - Creating directories and files necessary for the project.

3. **Running a Basic Python Script**
   - Writing a simple "Hello, World!" script.
   - Executing the script to ensure the environment is correctly set up.

4. **Project Folder Structure**
   - Detailed explanation of each directory and file in the project structure.
   - Creation of the initial project structure.

## Lesson Content

### 1. Introduction to Python

**Discussion Points:**
- Python is a high-level, interpreted programming language known for its readability and ease of use.
- It is widely used in web development, data science, automation, and more.
- Python's syntax is simple and its community is vast, offering extensive libraries and frameworks.

**Installation:**
- Guide students to install Python from [python.org](https://www.python.org/downloads/).
  - Ensure that Python is added to the system PATH during installation.
- Guide students to install Git from [git-scm.com](https://git-scm.com/).
  - After installation, verify by running:
    ```sh
    git --version
    ```
- Guide students to install Visual Studio Code from [code.visualstudio.com](https://code.visualstudio.com/).
  - After installation, students can open the project directory in VS Code and install recommended extensions for Python development.

### 2. Learing the Project Structure

**Discussion Points:**
- An organized project structure helps in maintaining the code and makes collaboration easier.
- We have created a project structure that separates different concerns like main application logic, data operations, and configurations.

**Activity:**
- Review the main project directory: `PersonalLibrary`.
- Inside `PersonalLibrary`, you should see the following structure:

  ```plaintext
    PersonalLibrary/
    ├── config.py
    ├── main.py
    ├── library/
    │   ├── __init__.py
    │   ├── book.py
    │   ├── data_operations/
    │   │   ├── __init__.py
    │   │   ├── base_operations.py
    │   │   ├── csv_operations.py
    │   │   ├── db_operations.py
    │   └── utils.py
    ├── data/
    │   ├── books.csv
    └── README.md
  ```
  
  **Understand the structure:**
- **config.py**: This file will contain any configuration settings for the project.
- **main.py**: The main entry point of the application. This is where the application logic starts.
- **library/**: This directory will contain the core logic of the library management system.
  - **__init__.py**: Marks the directory as a Python package.
  - **book.py**: Contains the `Book` class definition.
  - **data_operations/**: Contains the modules for data operations.
    - **__init__.py**: Marks the directory as a Python package.
  - **utils.py**: Contains utility functions and the factory pattern to switch between CSV and database operations.
- **data/**: Directory for storing data files like CSV files.
- **PythonLearningLibraryProject.code-workspace**: Where the VS code settings for this project are saved.
- **README.md**: Documentation file for the project.


### 3. Running a Basic Python Script

**Activity:**
- Create a simple "Hello, World!" script to ensure Python is set up correctly.
  
  **Code for `main.py`:**
  ```python
  print("Hello, World!")
  ```
- Run the script from the command line:
    ```cmd
    python main.py
    ```
- Expected Output:
    ```
    Hello, World!
    ```