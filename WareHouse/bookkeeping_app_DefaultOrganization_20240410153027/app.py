'''
This file contains the BookkeepingApp class which represents the bookkeeping application.
'''
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime
import matplotlib.pyplot as plt
class BookkeepingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bookkeeping App")
        self.root.geometry("800x600")
        self.income_expense_records = []
        self.categories = []
        self.budgets = []
        self.create_menu()
        self.create_tabs()
    def create_menu(self):
        menu_bar = tk.Menu(self.root)
        self.root.config(menu=menu_bar)
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Export Data", command=self.export_data)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        menu_bar.add_cascade(label="File", menu=file_menu)
    def create_tabs(self):
        tab_control = ttk.Notebook(self.root)
        record_tab = ttk.Frame(tab_control)
        self.create_record_tab(record_tab)
        tab_control.add(record_tab, text="Record")
        view_tab = ttk.Frame(tab_control)
        self.create_view_tab(view_tab)
        tab_control.add(view_tab, text="View")
        analyze_tab = ttk.Frame(tab_control)
        self.create_analyze_tab(analyze_tab)
        tab_control.add(analyze_tab, text="Analyze")
        budget_tab = ttk.Frame(tab_control)
        self.create_budget_tab(budget_tab)
        tab_control.add(budget_tab, text="Budget")
        tab_control.pack(expand=True, fill="both")
    def create_record_tab(self, record_tab):
        # Create labels and entry fields for bill type, amount, date, and notes
        bill_type_label = ttk.Label(record_tab, text="Bill Type:")
        bill_type_label.grid(row=0, column=0, padx=10, pady=10)
        self.bill_type_entry = ttk.Entry(record_tab)
        self.bill_type_entry.grid(row=0, column=1, padx=10, pady=10)
        amount_label = ttk.Label(record_tab, text="Amount:")
        amount_label.grid(row=1, column=0, padx=10, pady=10)
        self.amount_entry = ttk.Entry(record_tab)
        self.amount_entry.grid(row=1, column=1, padx=10, pady=10)
        date_label = ttk.Label(record_tab, text="Date:")
        date_label.grid(row=2, column=0, padx=10, pady=10)
        self.date_entry = ttk.Entry(record_tab)
        self.date_entry.grid(row=2, column=1, padx=10, pady=10)
        notes_label = ttk.Label(record_tab, text="Notes:")
        notes_label.grid(row=3, column=0, padx=10, pady=10)
        self.notes_entry = ttk.Entry(record_tab)
        self.notes_entry.grid(row=3, column=1, padx=10, pady=10)
        # Create a button to add the record
        add_button = ttk.Button(record_tab, text="Add Record", command=self.add_record)
        add_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
    def create_view_tab(self, view_tab):
        # Create a treeview to display the income and expense records
        self.treeview = ttk.Treeview(view_tab, columns=("Type", "Amount", "Date", "Notes"))
        self.treeview.heading("#0", text="ID")
        self.treeview.heading("Type", text="Type")
        self.treeview.heading("Amount", text="Amount")
        self.treeview.heading("Date", text="Date")
        self.treeview.heading("Notes", text="Notes")
        self.treeview.pack(expand=True, fill="both")
    def create_analyze_tab(self, analyze_tab):
        # Create a line chart to display the income and expense distribution
        x = [1, 2, 3, 4, 5]  # Example x-axis values
        y = [10, 15, 7, 12, 9]  # Example y-axis values
        plt.plot(x, y)
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')
        plt.title('Income and Expense Distribution')
        plt.grid(True)
        plt.show()
    def create_budget_tab(self, budget_tab):
        # Create labels and entry fields for budget amount and duration
        budget_amount_label = ttk.Label(budget_tab, text="Budget Amount:")
        budget_amount_label.grid(row=0, column=0, padx=10, pady=10)
        self.budget_amount_entry = ttk.Entry(budget_tab)
        self.budget_amount_entry.grid(row=0, column=1, padx=10, pady=10)
        budget_duration_label = ttk.Label(budget_tab, text="Budget Duration:")
        budget_duration_label.grid(row=1, column=0, padx=10, pady=10)
        self.budget_duration_entry = ttk.Entry(budget_tab)
        self.budget_duration_entry.grid(row=1, column=1, padx=10, pady=10)
        # Create a button to set the budget
        set_budget_button = ttk.Button(budget_tab, text="Set Budget", command=self.set_budget)
        set_budget_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
    def add_record(self):
        # Get the input values from the entry fields
        bill_type = self.bill_type_entry.get()
        amount = self.amount_entry.get()
        date = self.date_entry.get()
        notes = self.notes_entry.get()
        # Validate the input values
        if not bill_type or not amount or not date:
            messagebox.showerror("Error", "Please fill in all required fields.")
            return
        # Create a new record with the input values
        record = {
            "Type": bill_type,
            "Amount": amount,
            "Date": date,
            "Notes": notes
        }
        # Add the record to the income and expense records list
        self.income_expense_records.append(record)
        # Clear the entry fields
        self.bill_type_entry.delete(0, tk.END)
        self.amount_entry.delete(0, tk.END)
        self.date_entry.delete(0, tk.END)
        self.notes_entry.delete(0, tk.END)
        # Update the treeview with the new record
        record_id = len(self.income_expense_records)
        self.treeview.insert("", tk.END, text=str(record_id), values=(bill_type, amount, date, notes))
    def set_budget(self):
        # Get the input values from the entry fields
        budget_amount = self.budget_amount_entry.get()
        budget_duration = self.budget_duration_entry.get()
        # Validate the input values
        if not budget_amount or not budget_duration:
            messagebox.showerror("Error", "Please fill in all required fields.")
            return
        # Create a new budget with the input values
        budget = {
            "Amount": budget_amount,
            "Duration": budget_duration
        }
        # Add the budget to the budgets list
        self.budgets.append(budget)
        # Clear the entry fields
        self.budget_amount_entry.delete(0, tk.END)
        self.budget_duration_entry.delete(0, tk.END)
    def export_data(self):
        # Get the current date and time
        now = datetime.now()
        timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")
        # Create a file name with the timestamp
        file_name = f"bookkeeping_data_{timestamp}.csv"
        # Open the file in write mode
        with open(file_name, "w") as file:
            # Write the header row
            file.write("Type,Amount,Date,Notes\n")
            # Write each record as a new line
            for record in self.income_expense_records:
                line = f"{record['Type']},{record['Amount']},{record['Date']},{record['Notes']}\n"
                file.write(line)
        messagebox.showinfo("Export Data", f"Data exported to {file_name}")