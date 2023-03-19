import tkinter as tk
import tkinter.ttk as ttk

# สร้างหน้าต่าง
window = tk.Tk()
window.geometry("400x400")
window.title("ตารางเวันเดือนปี รายรับ-รายจ่าย")

# สร้างตาราง
columns = ("#1", "#2", "#3", "#4")
table = ttk.Treeview(window, show="headings", columns=columns)
table.heading("#1", text="วัน/เดือน/ปี")
table.heading("#2", text="รายรับ")
table.heading("#3", text="รายจ่าย")
table.heading("#4", text="เงินคงเหลือ")
table.pack()

# สร้างข้อความและช่องกรอกข้อมูล
date_label = tk.Label(window, text="วัน/เดือน/ปี:")
date_label.pack()

date_entry = tk.Entry(window)
date_entry.pack()

income_label = tk.Label(window, text="รายได้:")
income_label.pack()

income_entry = tk.Entry(window)
income_entry.pack()

expense_label = tk.Label(window, text="รายจ่าย:")
expense_label.pack()

expense_entry = tk.Entry(window)
expense_entry.pack()

# สร้างปุ่ม
def calculate():
    date = date_entry.get()
    income = float(income_entry.get())
    expense = float(expense_entry.get())
    balance = income - expense
    result_label.config(text="เงินที่เหลือ: {:.2f}".format(balance))
    
    # เพิ่มข้อมูลลงในตาราง
    table.insert("", "end", values=(date, income, expense, balance))

button = tk.Button(window, text="คำนวณ", command=calculate)
button.pack()

# สร้างป้ายผลลัพธ์
result_label = tk.Label(window, text="เงินที่เหลือ: 0.00")
result_label.pack()

# เริ่มการทำงานของโปรแกรม
window.mainloop()
