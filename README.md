# Automated Code Review Bot

## Overview
The **Automated Code Review Bot** is a Python-based tool that automatically analyzes code for quality, style, and security issues.  
It helps developers maintain consistent coding standards, reduces manual code review effort, and generates a **JSON report** with all findings.

### Key Features of the Bot
- Checks **code quality** (PEP8 compliance, unused imports, naming issues)  
- Enforces **style guide rules** using Flake8  
- Detects **security vulnerabilities** using Bandit  
- Generates a **structured JSON report** with detailed errors, warnings, and security issues  
- Can analyze **any folder containing Python files**  

---

## Tech Stack
- **Language:** Python 3.x  
- **Libraries/Tools:**  
  - `pylint` → Code quality & PEP8 compliance  
  - `flake8` → Style guide enforcement  
  - `bandit` → Security vulnerability detection  

---

## Folder Structure
Automated-Code-Review/
│
├── analyzer/ # Bot code
│ ├── init.py
│ └── checker.py
│
├── sample_code/ # Sample Python files for testing
│ └── sample1.py
│
├── requirements.txt # Required Python packages
├── report.json # Example output report
└── README.md

---

## Installation

### 1. Clone the repository

git clone https://github.com/Shubookumar7999/Automated-Code-Review.git
cd Automated-Code-Review

2. Create a virtual environment
Windows:
cmd:

python -m venv venv
venv\Scripts\activate
Mac/Linux:

python3 -m venv venv
source venv/bin/activate
3. Install dependencies

pip install -r requirements.txt
#How to Run the Bot
Run on sample code folder

python -m analyzer.checker sample_code
Mac/Linux:

python3 -m analyzer.checker sample_code
Run on any other folder

python -m analyzer.checker <folder_name>

#Output:
The bot prints results in JSON format in the terminal.
The same results are saved in report.json in the project folder.
