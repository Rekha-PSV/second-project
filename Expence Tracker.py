import sqlite3
from datetime import datetime

# Connect to the SQLite database
conn = sqlite3.connect('expenses.db')
c = conn.cursor()

# Create a table to store expenses
c.execute('''
CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY,
    date TEXT,
    category TEXT,
    amount REAL,
    description TEXT
)
''')

# Commit changes and close the connection to the database
conn.commit()

# Function to add an expense
def add_expense(date, category, amount, description):
    with conn:
        c.execute("INSERT INTO expenses (date, category, amount, description) VALUES (?, ?, ?, ?)",
                  (date, category, amount, description))

# Function to view all expenses
def view_expenses():
    with conn:
        c.execute("SELECT * FROM expenses")
        data = c.fetchall()
        for row in data:
          print(row)

# Function to view total expenses by category
def total_expenses_by_category(category):
    with conn:
        c.execute("SELECT SUM(amount) FROM expenses WHERE category = ?", (category,))
        total = c.fetchone()[0]
        print(f"Total spent on {category}: {total}")

# Main program
while True:
    print("\nExpense Tracker")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expenses by Category")
    print("4. Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        date = input("Enter date (YYYY-MM-DD): ")
        category = input("Enter category: ")
        amount = float(input("Enter amount: "))
        description = input("Enter description: ")
        add_expense(date, category, amount, description)
    elif choice == '2':
        view_expenses()
    elif choice == '3':
        category = input("Enter category: ")
        total_expenses_by_category(category)
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please try again")