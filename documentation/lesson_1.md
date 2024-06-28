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

### 2. Setting Up Your Own Fork of the Repository
Before you begin, you need to create your own fork of the repository. Follow the steps below:

1. **Fork the Repository:**
   - Go to the GitHub page of the repository: [PythonLearningLibraryProject](https://github.com/abnoba12/PythonLearningLibraryProject.git).
   - Click the "Fork" button at the top right of the page to create your own copy of the repository under your GitHub account.

2. **Clone Your Fork:**
   - Once you have forked the repository, clone your fork to your local machine. Replace `your-username` with your GitHub username:

   ```sh
   git clone https://github.com/your-username/PythonLearningLibraryProject.git
   ```
3. **Navigate to the Repository Directory:**
    ```sh
    cd PythonLearningLibraryProject
    ```
4. **Add Upstream Remote:**
   - To keep your fork up to date with the original repository, add the original repository as an upstream remote:
    ```sh
      git remote add upstream https://github.com/abnoba12/PythonLearningLibraryProject.git
    ```

### 3. Learing the Project Structure

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

## Moving to Lesson 2

If you have completed Lesson 1 and are ready to proceed to Lesson 2, you need to change your Git branch to `Lesson_2`. Follow the steps below to switch branches:

1. **Ensure all changes are committed:**
   Before switching branches, make sure you have committed all your changes in the current branch. You can do this with the following commands:

   ```sh
   git add .
   git commit -m "Completed Lesson 1"
   ```
2. **Fetch all branches:**
   ```sh
   Fetch all branches:
   ```
3. **Switch to the Lesson_2 branch:**
   To switch to the Lesson_2 branch, use the following command:

   ```sh
   git checkout Lesson_2
   ```
1. **Verify the branch switch:**
   You can verify that you have switched to the correct branch by running:

   ```sh
   git branch
   ```
   The output should show Lesson_2 with an asterisk (*) next to it, indicating that you are currently on this branch.
   ```sh
    * Lesson_2
      main
   ```
   Once you have switched to the Lesson_2 branch, you are ready to start the next lesson. Happy coding!