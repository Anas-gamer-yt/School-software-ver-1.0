# Python-Based School Management System

## Project
**The Little Angels Public Higher Secondary School**  
A Project by MK Group of Companies

Offline desktop software built with Python and Tkinter for student/staff/fee/expense/donation management with local JSON storage.

## Features
- Dashboard KPIs with quick navigation
- Students module with full profile fields, search/filter, PDF/CSV export
- Fees module with student-linked payments, payment method/status, receipt PDF
- Staff module with staff CRUD, salary payments, payment method/status, salary receipt PDF
- Expenses module with category tracking and receipt/report export
- Donations module with donor records, receipt PDF/print, and report export
- Direct receipt printing on Windows with native print dialog
- Sortable table headers + horizontal/vertical scrollbars across data-entry modules
- POS-style 58mm thermal receipt PDFs (monospaced, wrapped, printer-friendly)
- Reports module:
  - Student List
  - Fee Report
  - Staff Salary Report
  - Expense Report
  - Donation Report
  - Defaulter Report
  - Profit / Loss Report
- Info module for school details, logo, and receipt footer text
- Backup module:
  - ZIP backup of JSON files
  - Restore from ZIP
  - Backup log with timestamps and notes

## Tech Stack
- Python 3.x
- Tkinter
- JSON
- `fpdf2` for PDFs
- `Pillow` for image handling

## Run
```powershell
cd school_software
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

## Build EXE (PyInstaller)
```powershell
cd school_software
pip install pyinstaller
pyinstaller --onefile --windowed main.py --name SchoolSoftware
```

Build output will be in `dist/SchoolSoftware.exe`.

## Data Files
- `students.json`
- `fees.json`
- `staff.json`
- `expenses.json`
- `donations.json`
- `info.json`
- `backup/backup_log.json`

## Notes
- Designed for single-computer offline use.
- No SQL server required.
- Receipts are saved in `receipts/`.
- For direct printing, Windows must have a PDF viewer/app associated with `.pdf` print actions.
