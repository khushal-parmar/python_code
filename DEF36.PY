import tkinter as tk
from tkinter import ttk, messagebox

root = tk.Tk()
root.title("Employee Registration")
root.geometry("700x600")

employee_id = tk.StringVar()
first_name = tk.StringVar()
last_name = tk.StringVar()
gender = tk.StringVar()
dob = tk.StringVar()
phone = tk.StringVar()
email = tk.StringVar()
department = tk.StringVar()
designation = tk.StringVar()
joining_date = tk.StringVar()
salary = tk.StringVar()


def submit():
    address = address_text.get("1.0", tk.END).strip()

    if employee_id.get() == "":
        messagebox.showerror("Error", "Enter Employee ID")
        return

    if first_name.get() == "":
        messagebox.showerror("Error", "Enter First Name")
        return

    if last_name.get() == "":
        messagebox.showerror("Error", "Enter Last Name")
        return

    if gender.get() == "":
        messagebox.showerror("Error", "Select Gender")
        return

    if dob.get() == "":
        messagebox.showerror("Error", "Enter Date of Birth")
        return

    if phone.get() == "":
        messagebox.showerror("Error", "Enter Phone")
        return

    if email.get() == "":
        messagebox.showerror("Error", "Enter Email")
        return

    if address == "":
        messagebox.showerror("Error", "Enter Address")
        return

    if department.get() == "":
        messagebox.showerror("Error", "Select Department")
        return

    if designation.get() == "":
        messagebox.showerror("Error", "Enter Designation")
        return

    if joining_date.get() == "":
        messagebox.showerror("Error", "Enter Joining Date")
        return

    if salary.get() == "":
        messagebox.showerror("Error", "Enter Salary")
        return

    messagebox.showinfo(
        "Success",
        "Employee Registered Successfully!"
    )

    employee_id.set("")
    first_name.set("")
    last_name.set("")
    gender.set("")
    dob.set("")
    phone.set("")
    email.set("")
    department.set("")
    designation.set("")
    joining_date.set("")
    salary.set("")

    address_text.delete("1.0", tk.END)


tk.Label(
    root,
    text="EMPLOYEE REGISTRATION",
    font=("Arial", 20, "bold")
).pack(pady=20)


tk.Label(root, text="Employee ID").place(x=50, y=80)
tk.Entry(root, textvariable=employee_id).place(x=180, y=80)

tk.Label(root, text="First Name").place(x=370, y=80)
tk.Entry(root, textvariable=first_name).place(x=490, y=80)


tk.Label(root, text="Last Name").place(x=50, y=125)
tk.Entry(root, textvariable=last_name).place(x=180, y=125)

tk.Label(root, text="Gender").place(x=370, y=125)
ttk.Combobox(
    root,
    textvariable=gender,
    values=["Male", "Female", "Other"],
    state="readonly"
).place(x=490, y=125)


tk.Label(root, text="Date of Birth").place(x=50, y=170)
tk.Entry(root, textvariable=dob).place(x=180, y=170)

tk.Label(root, text="Phone").place(x=370, y=170)
tk.Entry(root, textvariable=phone).place(x=490, y=170)


tk.Label(root, text="Email").place(x=50, y=215)
tk.Entry(root, textvariable=email).place(x=180, y=215)

tk.Label(root, text="Address").place(x=370, y=215)

address_text = tk.Text(root, width=20, height=3)
address_text.place(x=490, y=215)


tk.Label(root, text="Department").place(x=50, y=280)

ttk.Combobox(
    root,
    textvariable=department,
    values=[
        "HR",
        "IT",
        "Finance",
        "Sales",
        "Marketing"
    ],
    state="readonly"
).place(x=180, y=280)


tk.Label(root, text="Designation").place(x=370, y=280)
tk.Entry(root, textvariable=designation).place(x=490, y=280)


tk.Label(root, text="Joining Date").place(x=50, y=325)
tk.Entry(root, textvariable=joining_date).place(x=180, y=325)

tk.Label(root, text="Salary").place(x=370, y=325)
tk.Entry(root, textvariable=salary).place(x=490, y=325)


tk.Button(
    root,
    text="SUBMIT",
    command=submit,
    width=20
).place(x=280, y=400)


root.mainloop()   