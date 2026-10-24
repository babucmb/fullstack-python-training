"""Employee Payroll System - a small Python + FastAPI learning project's."""
import csv
import io
from datetime import date, datetime
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
from html import escape
from typing import Optional

from fastapi import FastAPI, Form, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse, StreamingResponse

app = FastAPI(title="Employee Payroll System", description="A simple payroll calculator built to practise Python concepts.", version="1.0.0")

# In-memory lists: no external database or file storage is used.
employees = []
payroll_records = []
next_employee_id = 1
next_payroll_id = 1


def money(value) -> Decimal:
    """Convert a value to a 2-decimal-place Decimal safely."""
    try:
        amount = Decimal(str(value)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    except (InvalidOperation, ValueError, TypeError):
        raise ValueError("Enter a valid numeric amount.")
    if not amount.is_finite() or amount < 0:
        raise ValueError("Amounts must be valid, non-negative numbers.")
    return amount


class Employee:
    """Represent one employee (class, object, attributes and methods)."""
    def __init__(self, employee_id: int, name: str, department: str, role: str, monthly_basic: Decimal):
        self.employee_id = employee_id
        self.name = name.strip()
        self.department = department.strip()
        self.role = role.strip()
        self.monthly_basic = monthly_basic
        self.joined_on = date.today()
        self.active = True


class PayrollCalculator:
    """Calculate a sample monthly salary using basic Python arithmetic."""
    def calculate(self, basic, allowances, bonus, deductions, overtime=0, leave_deduction=0):
        basic, allowances, bonus, deductions, overtime, leave_deduction = map(
            money, (basic, allowances, bonus, deductions, overtime, leave_deduction)
        )
        gross = basic + allowances + bonus + overtime
        total_deductions = deductions + leave_deduction
        if total_deductions > gross:
            raise ValueError("Deductions cannot be greater than gross salary.")
        return {
            "basic": basic,
            "allowances": allowances,
            "bonus": bonus,
            "overtime": overtime,
            "gross": gross,
            "other_deductions": deductions,
            "leave_deduction": leave_deduction,
            "deductions": total_deductions,
            "net": gross - total_deductions,
        }


calculator = PayrollCalculator()


def page(content: str, title: str = "Employee Payroll System") -> HTMLResponse:
    """Return a small responsive HTML page; no separate frontend framework needed."""
    return HTMLResponse(f'''
    <!doctype html>
    <html lang="en">
    <head> 
    <meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{escape(title)}</title>
    <style>
    *{{box-sizing:border-box}}
    body{{margin:0;background:#f3f6fb;color:#172033;font:15px Arial,sans-serif}}
    header{{background:#173b67;color:white;padding:22px max(20px,calc((100% - 1080px)/2))}}
    header h1{{margin:0 0 8px;font-size:25px}}
    nav{{display:flex;gap:16px;flex-wrap:wrap;margin-top:12px}}
    nav a{{color:#dceaff;text-decoration:none}}
    main{{max-width:1080px;margin:26px auto;padding:0 18px}}
    @media print{{header,footer,.no-print{{display:none!important}}body{{background:#fff}}main{{max-width:none;margin:0;padding:0}}.card{{box-shadow:none;border:0}}}}
    .card{{background:white;border:1px solid #e1e7f0;border-radius:12px;padding:20px;margin-bottom:18px;box-shadow:0 3px 12px #17203308}}
    .grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(210px,1fr));gap:14px}}
    label{{display:block;font-weight:600;margin:10px 0 5px}}input,select{{width:100%;padding:10px;border:1px solid #cbd5e1;border-radius:7px;font:inherit}}
    button,.button{{display:inline-block;border:0;border-radius:7px;padding:11px 15px;background:#1765b3;color:white;font-weight:600;text-decoration:none;cursor:pointer;margin-top:14px}}
    .muted{{color:#64748b}}.stats{{font-size:25px;font-weight:700;margin-top:8px}}.message{{padding:12px;background:#fff7df;border-radius:8px}}
    table{{border-collapse:collapse;width:100%;margin-top:12px}}th,td{{padding:10px;text-align:left;border-bottom:1px solid #e2e8f0}}
    th{{background:#f8fafc}}.table-wrap{{overflow-x:auto}}.pill{{padding:4px 8px;background:#e2f8e9;border-radius:20px;color:#166534}}
    footer{{text-align:center;color:#64748b;padding:20px}}@media(max-width:600px){{header h1{{font-size:21px}}th,td{{padding:8px;font-size:13px}}}}
    </style>
    </head>
    <body>
    <header>
        <h1>Employee Payroll System</h1>
        <div>Employee payroll creation · FastAPI · Payroll calculator</div>
        <nav>
            <a href="/">Dashboard</a>
            <a href="/employees">Employees</a>
            <a href="/employees/new">Add Employee</a>
            <a href="/payroll/new">Calculate Payroll</a>
            <a href="/payroll/history">Payroll History</a>
            <a href="/docs">API Docs</a>
        </nav>
        </header>
            <main>{content}</main>
            <footer>Learning project · Data stays in memory and resets when the server restarts.</footer>
            </body>
    </html>''')


def employee_by_id(employee_id: int) -> Optional[Employee]:
    for employee in employees:
        if employee.employee_id == employee_id:
            return employee
    return None


@app.get("/", response_class=HTMLResponse)
def dashboard():
    active_count = sum(1 for employee in employees if employee.active)
    total_net = sum((record["net"] for record in payroll_records), Decimal("0.00"))
    recent = sorted(payroll_records, key=lambda item: item["created_at"], reverse=True)[:5]
    recent_rows = "".join(f"<tr><td>{r['payroll_id']}</td><td>{escape(r['employee_name'])}</td><td>{escape(r['month'])}</td><td>₹{r['net']:.2f}</td></tr>" for r in recent)
    if not recent_rows:
        recent_rows = '<tr><td colspan="4" class="muted">No payroll records yet. Calculate a payroll to see it here.</td></tr>'
    return page(f'''<section class="grid">
                        <div class="card">
                            <div class="muted">Active employees</div>
                            <div class="stats">{active_count}</div>
                        </div>
                        <div class="card">
                            <div class="muted">Payroll calculations</div>
                            <div class="stats">{len(payroll_records)}</div>
                        </div>
                        <div class="card">
                            <div class="muted">Total net pay calculated</div>
                            <div class="stats">₹{total_net:.2f}</div>
                        </div>
                    </section>
                    <section class="card">
                        <h2>Welcome</h2> <p>A Python and FastAPI application designed to manage employee records, calculate monthly salaries, apply allowances and deductions, and maintain payroll summaries.</p>
                        <p class="message">This is a learning demo, not a production payroll product. Data is held in memory; there is no external database.</p>
                        <a class="button" href="/employees/new">+ Add Employee</a>
                        <a class="button" href="/payroll/new">Calculate Payroll</a>
                    </section>
                    <section class="card">
                        <h2>Recent payroll calculations</h2>
                        <div class="table-wrap">
                            <table>
                            <thead> <tr><th>ID</th><th>Employee</th><th>Month</th><th>Net salary</th></tr></thead>
                            <tbody>{recent_rows}</tbody></table>
                        </div>
                    </section>''')


@app.get("/employees", response_class=HTMLResponse)
def list_employees(search: str = "", department: str = "", status: str = ""):
    departments = sorted({e.department for e in employees}, key=str.casefold)
    filtered = [
        e for e in employees
        if search.strip().casefold() in e.name.casefold()
        and (not department or e.department == department)
        and (status not in ("active", "inactive") or e.active == (status == "active"))
    ]
    department_options = '<option value="">All departments</option>' + "".join(
        f'<option value="{escape(value, quote=True)}"{" selected" if value == department else ""}>{escape(value)}</option>'
        for value in departments
    )
    rows = "".join(
        f'''<tr><td>{e.employee_id}</td><td>{escape(e.name)}</td><td>{escape(e.department)}</td><td>{escape(e.role)}</td><td>₹{e.monthly_basic:.2f}</td><td>{e.joined_on.isoformat()}</td><td>{'Active' if e.active else 'Inactive'}</td><td><a href="/employees/{e.employee_id}/edit">Edit</a><form class="no-print" method="post" action="/employees/{e.employee_id}/{"deactivate" if e.active else "reactivate"}" style="display:inline"><button type="submit">{"Deactivate" if e.active else "Reactivate"}</button></form></td></tr>'''
        for e in filtered
    )
    if not rows:
        rows = '<tr><td colspan="8" class="muted">No matching employees found.</td></tr>'
    return page(f'''<section class="card"><h2>Employee Directory</h2><p class="muted">Employee details are stored in a Python list while the server is running.</p><a class="button" href="/employees/new">+ Add Employee</a><form method="get" action="/employees"><div class="grid"><div><label>Search by name</label><input type="search" name="search" value="{escape(search, quote=True)}" placeholder="Employee name"></div><div><label>Department</label><select name="department">{department_options}</select></div><div><label>Status</label><select name="status"><option value=""{" selected" if not status else ""}>All statuses</option><option value="active"{" selected" if status == "active" else ""}>Active</option><option value="inactive"{" selected" if status == "inactive" else ""}>Inactive</option></select></div></div><button type="submit">Filter employees</button> <a class="button" href="/employees">Clear filters</a></form><div class="table-wrap"><table><thead><tr><th>ID</th><th>Name</th><th>Department</th><th>Role</th><th>Basic salary</th><th>Joined</th><th>Status</th><th>Actions</th></tr></thead><tbody>{rows}</tbody></table></div></section>''')


@app.get("/employees/new", response_class=HTMLResponse)
def new_employee_form():
    return page('''<section class="card"><h2>Add Employee</h2><form method="post" action="/employees"><div class="grid"><div><label>Full name *</label><input name="name" required maxlength="80" placeholder="e.g. Ravi Kumar"></div><div><label>Department *</label><input name="department" required maxlength="60" placeholder="e.g. Finance"></div><div><label>Job role *</label><input name="role" required maxlength="60" placeholder="e.g. Junior Analyst"></div><div><label>Monthly basic salary (₹) *</label><input name="monthly_basic" type="number" min="0" step="0.01" required placeholder="25000"></div></div><button type="submit">Save Employee</button></form></section>''')


@app.post("/employees")
def add_employee(name: str = Form(...), department: str = Form(...), role: str = Form(...), monthly_basic: str = Form(...)):
    global next_employee_id
    if not name.strip() or not department.strip() or not role.strip():
        raise HTTPException(status_code=400, detail="Name, department and role are required.")
    if any(e.name.casefold() == name.strip().casefold() and e.active for e in employees):
        return page('<section class="card"><h2>Employee not added</h2><p class="message">An active employee with this name already exists in this demo.</p><a class="button" href="/employees/new">Go back</a></section>')
    try:
        basic = money(monthly_basic)
    except ValueError as exc:
        return page(f'<section class="card"><h2>Invalid salary</h2><p class="message">{escape(str(exc))}</p><a class="button" href="/employees/new">Go back</a></section>')
    employees.append(Employee(next_employee_id, name, department, role, basic))
    next_employee_id += 1
    return RedirectResponse("/employees", status_code=303)


@app.get("/employees/{employee_id}/edit", response_class=HTMLResponse)
def edit_employee_form(employee_id: int):
    employee = employee_by_id(employee_id)
    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found.")
    return page(f'''<section class="card"><h2>Edit Employee</h2><form method="post" action="/employees/{employee_id}/edit"><div class="grid"><div><label>Full name *</label><input name="name" required maxlength="80" value="{escape(employee.name, quote=True)}"></div><div><label>Department *</label><input name="department" required maxlength="60" value="{escape(employee.department, quote=True)}"></div><div><label>Job role *</label><input name="role" required maxlength="60" value="{escape(employee.role, quote=True)}"></div><div><label>Monthly basic salary (₹) *</label><input name="monthly_basic" type="number" min="0" step="0.01" required value="{employee.monthly_basic:.2f}"></div></div><button type="submit">Save Changes</button> <a class="button" href="/employees">Cancel</a></form></section>''')


@app.post("/employees/{employee_id}/edit")
def update_employee(employee_id: int, name: str = Form(...), department: str = Form(...), role: str = Form(...), monthly_basic: str = Form(...)):
    employee = employee_by_id(employee_id)
    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found.")
    if not name.strip() or not department.strip() or not role.strip():
        return page('<section class="card"><h2>Employee not updated</h2><p class="message">Name, department and role are required.</p><a class="button" href="/employees/' + str(employee_id) + '/edit">Try again</a></section>')
    if any(e.employee_id != employee_id and e.name.casefold() == name.strip().casefold() and e.active for e in employees):
        return page('<section class="card"><h2>Employee not updated</h2><p class="message">An active employee with this name already exists in this demo.</p><a class="button" href="/employees/' + str(employee_id) + '/edit">Try again</a></section>')
    try:
        basic = money(monthly_basic)
    except ValueError as exc:
        return page(f'<section class="card"><h2>Invalid salary</h2><p class="message">{escape(str(exc))}</p><a class="button" href="/employees/{employee_id}/edit">Try again</a></section>')
    employee.name = name.strip()
    employee.department = department.strip()
    employee.role = role.strip()
    employee.monthly_basic = basic
    return RedirectResponse("/employees", status_code=303)


@app.post("/employees/{employee_id}/deactivate")
def deactivate_employee(employee_id: int):
    employee = employee_by_id(employee_id)
    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found.")
    employee.active = False
    return RedirectResponse("/employees", status_code=303)


@app.post("/employees/{employee_id}/reactivate")
def reactivate_employee(employee_id: int):
    employee = employee_by_id(employee_id)
    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found.")
    if any(e.employee_id != employee_id and e.name.casefold() == employee.name.casefold() and e.active for e in employees):
        return page('<section class="card"><h2>Employee not reactivated</h2><p class="message">An active employee with this name already exists in this demo.</p><a class="button" href="/employees">Back to employees</a></section>')
    employee.active = True
    return RedirectResponse("/employees", status_code=303)


@app.get("/payroll/new", response_class=HTMLResponse)
def payroll_form():
    active = [e for e in employees if e.active]
    if not active:
        return page('<section class="card"><h2>Calculate Payroll</h2><p class="message">Add an employee before calculating payroll.</p><a class="button" href="/employees/new">Add Employee</a></section>')
    options = "".join(f'<option value="{e.employee_id}">{e.employee_id} - {escape(e.name)} (₹{e.monthly_basic:.2f} basic)</option>' for e in active)
    current_month = date.today().strftime("%Y-%m")
    return page(f'''<section class="card"><h2>Payroll Calculator</h2><p class="muted">Basic salary is taken from the employee record. Add overtime pay and any leave deduction as needed.</p><form method="post" action="/payroll"><label>Employee *</label><select name="employee_id" required>{options}</select><div class="grid"><div><label>Payroll month *</label><input type="month" name="month" value="{current_month}" required></div><div><label>Allowances (₹)</label><input type="number" name="allowances" min="0" step="0.01" value="0" required></div><div><label>Bonus (₹)</label><input type="number" name="bonus" min="0" step="0.01" value="0" required></div><div><label>Overtime pay (₹)</label><input type="number" name="overtime" min="0" step="0.01" value="0" required></div><div><label>Other deductions (₹)</label><input type="number" name="deductions" min="0" step="0.01" value="0" required></div><div><label>Leave deduction (₹)</label><input type="number" name="leave_deduction" min="0" step="0.01" value="0" required></div></div><button type="submit">Calculate and Save</button></form></section>''')


@app.post("/payroll", response_class=HTMLResponse)
def calculate_payroll(employee_id: int = Form(...), month: str = Form(...), allowances: str = Form("0"), bonus: str = Form("0"), deductions: str = Form("0"), overtime: str = Form("0"), leave_deduction: str = Form("0")):
    global next_payroll_id
    employee = employee_by_id(employee_id)
    if employee is None or not employee.active:
        return page('<section class="card"><h2>Unable to calculate payroll</h2><p class="message">Choose an active employee.</p><a class="button" href="/payroll/new">Try again</a></section>')
    try:
        datetime.strptime(month, "%Y-%m")
        if any(record["employee_id"] == employee_id and record["month"] == month for record in payroll_records):
            return page(f'<section class="card"><h2>Payroll already exists</h2><p class="message">Payroll has already been calculated for {escape(employee.name)} in {escape(month)}. A second record was not created.</p><a class="button" href="/payroll/history">View history</a> <a class="button" href="/payroll/new">Back to payroll</a></section>')
        result = calculator.calculate(employee.monthly_basic, allowances, bonus, deductions, overtime, leave_deduction)
    except (ValueError, TypeError) as exc:
        return page(f'<section class="card"><h2>Check your inputs</h2><p class="message">{escape(str(exc))}</p><a class="button" href="/payroll/new">Try again</a></section>')
    record = {"payroll_id": next_payroll_id, "employee_id": employee.employee_id, "employee_name": employee.name, "department": employee.department, "role": employee.role, "month": month, **result, "created_at": datetime.now()}
    payroll_records.append(record)
    next_payroll_id += 1
    rows = "".join(f'<tr><th>{escape(label)}</th><td>₹{result[key]:.2f}</td></tr>' for label, key in [("Basic salary", "basic"), ("Allowances", "allowances"), ("Bonus", "bonus"), ("Overtime pay", "overtime"), ("Gross salary", "gross"), ("Other deductions", "other_deductions"), ("Leave deduction", "leave_deduction"), ("Total deductions", "deductions"), ("Net salary", "net")])
    return page(f'''<section class="card"><h2>Payroll Calculated Successfully</h2><p><strong>Employee:</strong> {escape(employee.name)} &nbsp; <strong>Month:</strong> {escape(month)}</p><div class="table-wrap"><table><tbody>{rows}</tbody></table></div><p class="message">Net salary: <strong>₹{result['net']:.2f}</strong></p><a class="button" href="/payroll/{record['payroll_id']}/payslip">View printable payslip</a> <a class="button" href="/payroll/new">Calculate another</a> <a class="button" href="/payroll/history">View history</a></section>''')


@app.get("/payroll/history", response_class=HTMLResponse)
def payroll_history():
    rows = "".join(f'''<tr><td>{r['payroll_id']}</td><td>{escape(r['employee_name'])}</td><td>{escape(r['department'])}</td><td>{escape(r['month'])}</td><td>₹{r['gross']:.2f}</td><td>₹{r['deductions']:.2f}</td><td><strong>₹{r['net']:.2f}</strong></td><td>{r['created_at'].strftime('%d %b %Y %H:%M')}</td><td><a href="/payroll/{r['payroll_id']}/payslip">Payslip</a></td></tr>''' for r in reversed(payroll_records))
    if not rows:
        rows = '<tr><td colspan="9" class="muted">No payroll calculations saved yet.</td></tr>'
    return page(f'''<section class="card"><h2>Payroll History</h2><p class="muted">Shows calculations created during this server session.</p><a class="button no-print" href="/payroll/export.csv">Export CSV</a><div class="table-wrap"><table><thead><tr><th>ID</th><th>Employee</th><th>Department</th><th>Month</th><th>Gross</th><th>Deductions</th><th>Net pay</th><th>Created</th><th>Actions</th></tr></thead><tbody>{rows}</tbody></table></div></section>''')


@app.get("/payroll/export.csv")
def export_payroll_csv():
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(["Payroll ID", "Employee ID", "Employee", "Department", "Role", "Month", "Basic", "Allowances", "Bonus", "Overtime", "Gross", "Other deductions", "Leave deduction", "Total deductions", "Net", "Created"])
    for record in payroll_records:
        text_fields = (record["employee_name"], record["department"], record["role"], record["month"])
        safe_text_fields = [
            "'" + value if value.lstrip(" \t\r\n")[:1] in ("=", "+", "-", "@") else value
            for value in text_fields
        ]
        writer.writerow([
            record["payroll_id"], record["employee_id"], *safe_text_fields,
            record["basic"], record["allowances"], record["bonus"],
            record["overtime"], record["gross"], record["other_deductions"], record["leave_deduction"],
            record["deductions"], record["net"], record["created_at"].isoformat(timespec="seconds"),
        ])
    return StreamingResponse(
        iter([output.getvalue()]),
        media_type="text/csv",
        headers={"Content-Disposition": 'attachment; filename="payroll-history.csv"'},
    )


@app.get("/payroll/{payroll_id}/payslip", response_class=HTMLResponse)
def payroll_payslip(payroll_id: int):
    record = next((item for item in payroll_records if item["payroll_id"] == payroll_id), None)
    if record is None:
        raise HTTPException(status_code=404, detail="Payroll record not found.")
    rows = "".join(
        f'<tr><th>{escape(label)}</th><td>₹{record[key]:.2f}</td></tr>'
        for label, key in [
            ("Basic salary", "basic"), ("Allowances", "allowances"), ("Bonus", "bonus"),
            ("Overtime pay", "overtime"), ("Gross salary", "gross"),
            ("Other deductions", "other_deductions"), ("Leave deduction", "leave_deduction"),
            ("Total deductions", "deductions"),
            ("Net salary", "net"),
        ]
    )
    return page(f'''<section class="card"><h2>Payroll Payslip</h2><p><strong>Employee:</strong> {escape(record['employee_name'])}</p><p><strong>Department:</strong> {escape(record['department'])} &nbsp; <strong>Role:</strong> {escape(record['role'])}</p><p><strong>Payroll month:</strong> {escape(record['month'])} &nbsp; <strong>Payroll ID:</strong> {record['payroll_id']}</p><div class="table-wrap"><table><tbody>{rows}</tbody></table></div><p class="muted">Generated {record['created_at'].strftime('%d %b %Y %H:%M')}</p><button class="no-print" onclick="window.print()">Print / Save as PDF</button> <a class="button no-print" href="/payroll/history">Back to history</a></section>''', title="Payroll Payslip")


@app.get("/api/employees")
def api_employees():
    """Example JSON endpoint, useful for learning FastAPI APIs."""
    return [{"id": e.employee_id, "name": e.name, "department": e.department, "role": e.role, "monthly_basic": str(e.monthly_basic), "joined_on": e.joined_on.isoformat(), "active": e.active} for e in employees]


@app.get("/api/payroll/history")
def api_payroll_history():
    return [{"payroll_id": r["payroll_id"], "employee_name": r["employee_name"], "month": r["month"], "basic": str(r["basic"]), "allowances": str(r["allowances"]), "bonus": str(r["bonus"]), "overtime": str(r["overtime"]), "gross": str(r["gross"]), "other_deductions": str(r["other_deductions"]), "leave_deduction": str(r["leave_deduction"]), "deductions": str(r["deductions"]), "net": str(r["net"]), "created_at": r["created_at"].isoformat(timespec="seconds")} for r in payroll_records]
