# Employee Payroll's System

A small Python learning project built with **FastAPI**. It demonstrates Python fundamentals through employee records and a monthly payroll calculator. It is intentionally not a production payroll product.

## Features

- Add employees with name, department, role, and monthly basic salary.
- Edit and deactivate employees without deleting their payroll history; reactivate them later.
- Search employees by name and filter the directory by department and active status.
- Calculate monthly payroll using basic salary, allowances, bonus, overtime pay, and deductions.
- Prevent duplicate payroll calculations for the same employee and month.
- Display gross salary, total deductions, and net salary.
- Keep a payroll history for the current run of the application.
- Export payroll history to CSV and view/print individual payslips.
- Dashboard counts for employees and payroll calculations.
- JSON endpoints for employee data and payroll history.
- Input validation and clear messages for invalid values.
- No external database, no unit-testing setup, no AI/ML.

## Salary formula

- **Gross salary** = Basic salary + Allowances + Bonus + Overtime pay
- **Total deductions** = Other deductions + Leave deduction
- **Net salary** = Gross salary - Total deductions

The calculator rejects negative amounts and deductions greater than gross salary. This is a learning example, not a statutory tax or compliance calculator.

## Project structure

```text
Employee-Payroll-System/
├── main.py           # FastAPI routes, Employee class, PayrollCalculator, page templates
├── requirements.txt  # Project dependencies
├── README.md         # Setup, features, concepts and usage
└── .gitignore
```

## Setup on Windows PowerShell

1. Extract the ZIP and open the `Employee-Payroll-System` folder in VS Code.
2. Open the VS Code terminal.
3. Create and activate a virtual environment:

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

4. Install dependencies:

   ```powershell
   python -m pip install -r requirements.txt
   ```

5. Run the server:

   ```powershell
   uvicorn main:app --reload
   ```

6. Open **http://127.0.0.1:8000** in your browser.
7. Open **http://127.0.0.1:8000/docs** to explore the FastAPI API documentation.

Stop the server with `Ctrl + C` in the terminal.

## How to use

1. Select **Add Employee** and create one or more employee records.
2. Open **Calculate Payroll**.
3. Select an employee and payroll month.
4. Enter allowances, bonus, overtime pay, and any other or leave deductions.
5. Submit to view the calculation.
6. Open **Payroll History** to review calculations from the current run.
7. Use **Export CSV** on the payroll history page or open a payslip to print/save it as a PDF.

## Python concepts demonstrated

- **Classes and objects:** `Employee`, `PayrollCalculator`
- **Encapsulation through methods:** `PayrollCalculator.calculate()`
- **Lists and dictionaries:** in-memory employee and payroll collections
- **Functions:** validation, lookup and page-rendering helpers
- **Loops and conditions:** searching employees and building tables
- **Exception handling:** invalid amounts and payroll input errors
- **Date and time:** employee joining date, payroll month and calculation timestamp
- **Decimal arithmetic:** avoids common floating-point money rounding issues
- **Type hints and optional values:** function definitions
- **String formatting and HTML escaping:** rendering values safely in pages
- **FastAPI:** routes, form inputs, JSON responses and interactive API docs

## Data storage limitation

Employee and payroll data are stored in Python lists in memory. They are cleared when the server restarts. No SQLite, cloud database, or external database is used.

## Current limitations

- Employee and payroll data are held in memory and reset when the server restarts.
- Overtime and leave are entered as monetary adjustments; this project does not calculate them from hours or attendance.
- Printable payslips use the browser's print dialog rather than generating a PDF file directly.
