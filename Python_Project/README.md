# University Management System

A small Streamlit application for keeping track of colleges, their students, and their teachers.

## Features

- Create colleges
- Add students with roll number, name, and branch
- Add teachers with name, branch, and subject
- View students and teachers for each college
- View a summary of all colleges
- Prevent duplicate college names and duplicate student roll numbers within a college

## Requirements

- Python 3.10 or newer
- The dependencies in `requirements.txt`

## Run locally

From this project folder, create and activate a virtual environment (optional but recommended), install dependencies, then start Streamlit:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
streamlit run main.py
```

Streamlit will print a local URL (normally `http://localhost:8501`) to open in your browser.

## Notes

The data is held in the active Streamlit session. Refreshing the browser or restarting the app clears the entries; this version does not use a database.
