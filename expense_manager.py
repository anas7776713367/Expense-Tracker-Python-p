import os
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt

FILE_NAME = "data.csv"


# Create the file if it does not exist
def create_file():
    if not os.path.exists(FILE_NAME):
        columns = ["Date", "Category", "Expense"]
        pd.DataFrame(columns=columns).to_csv(
            FILE_NAME,
            index=False,
            encoding="utf-8-sig"
        )


# Add a new expense
def add_amount():

    try:
        amount = float(input("Enter the amount: "))
    except ValueError:
        print("❌ The amount must be a number.")
        return

    category = input("Enter the category: ")

    date = dt.datetime.now().strftime("%Y-%m-%d %H:%M")

    new_data = pd.DataFrame([{
        "Date": date,
        "Category": category,
        "Expense": amount
    }])

    new_data.to_csv(
        FILE_NAME,
        mode="a",
        header=False,
        index=False,
        encoding="utf-8-sig"
    )

    print("✅ Expense added successfully.")


# Display all expenses
def view_amount():

    data = pd.read_csv(FILE_NAME)

    if data.empty:
        print("No data available.")
    else:
        print(data)


# Calculate total expenses
def total_amount():

    data = pd.read_csv(FILE_NAME)

    print(f"\nTotal Expenses = {data['Expense'].sum():.2f}")


# Display charts
def graphical():

    data = pd.read_csv(FILE_NAME)

    if data.empty:
        print("No data available for plotting.")
        return

    # Pie Chart
    data.groupby("Category")["Expense"].sum().plot(
        kind="pie",
        autopct="%1.1f%%",
        figsize=(6, 6)
    )

    plt.title("Expense Distribution by Category")
    plt.ylabel("")
    plt.show()

    # Bar Chart
    data.groupby("Category")["Expense"].sum().plot(
        kind="bar",
        figsize=(7, 5)
    )

    plt.title("Total Expenses by Category")
    plt.xlabel("Category")
    plt.ylabel("Amount")
    plt.grid(axis="y")
    plt.show()


# ----------------------------

create_file()

while True:

    print("""
========== Expense Management ==========
1- Add Expense
2- View Expenses
3- Total Expenses
4- Show Charts
5- Exit
========================================
""")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_amount()

    elif choice == "2":
        view_amount()

    elif choice == "3":
        total_amount()

    elif choice == "4":
        graphical()

    elif choice == "5":
        print("Program terminated.")
        break

    else:
        print("❌ Invalid choice.")
