import os
import csv
import argparse
from pathlib import Path
from datetime import datetime
from prettytable import PrettyTable

expense_DIR = Path(__file__).parent / "data"
expense_DIR.mkdir(exist_ok=True)
filename = expense_DIR / "expenses.csv"
fields = ['ID', 'Date', 'Description', 'Amount']

def add_expense(filename, description, amount):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            try:
                reader = csv.DictReader(file)
                expenses = list(reader)
            except csv.Error:
                expenses = []
    else:
        expenses = []
    
    next_id = (max((int(e["ID"]) for e in expenses), default=0)) + 1

    expense = {
        "ID": next_id, "Date": datetime.now().strftime("%Y-%m-%d"), "Description": description, "Amount": amount
    }
        
    expenses.append(expense)
        
    with open(filename, "w") as file:
        csvwriter = csv.DictWriter(file, fieldnames=fields)
        csvwriter.writeheader()
        csvwriter.writerows(expenses)
        
    print(expense)
    
def list_expenses(filename):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            try:
                reader = csv.DictReader(file)
                expenses = list(reader)
            except csv.Error:
                expenses = []
    else:
        expenses = []
        
    tab = PrettyTable(fields)
    for expense in expenses:
        tab.add_row([expense['ID'], expense['Date'], expense['Description'], expense['Amount']])
    print(tab)
    
def summary(filename, month=None):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            try:
                reader = csv.DictReader(file)
                expenses = list(reader)
            except csv.Error:
                expenses = []
    else:
        expenses = []
    
    if month:
        filtered_expenses = []
        for expense in expenses:
            expense_date = datetime.strptime(expense['Date'], "%Y-%m-%d")
            if expense_date.month == month:
                filtered_expenses.append(expense)
        expenses = filtered_expenses
    
    sum_expenses = []
    for expense in expenses:
        sum_expenses.append(float(expense['Amount']))
    print(f"${sum(sum_expenses)}")
    
def delete(filename, id):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            try:
                reader = csv.DictReader(file)
                expenses = list(reader)
            except csv.Error:
                expenses = []
    else:
        expenses = []
    
    expenses = [e for e in expenses if int(e['ID']) != int(id)]
    
    with open(filename, "w") as file:
        csvwriter = csv.DictWriter(file, fieldnames=fields)
        csvwriter.writeheader()
        csvwriter.writerows(expenses)
        
    print(f"Expense with ID {id} deleted.")
    
def update(filename, id, description, amount):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            try:
                reader = csv.DictReader(file)
                expenses = list(reader)
            except csv.Error:
                expenses = []
    else:
        expenses = []
        
    for expense in expenses:
        if int(expense['ID']) == int(id):
            expense['Description'] = description
            expense['Amount'] = amount
            expense['Date'] = datetime.now().strftime("%Y-%m-%d")
            break
        
    with open(filename, "w") as file:
        csvwriter = csv.DictWriter(file, fieldnames=fields)
        csvwriter.writeheader()
        csvwriter.writerows(expenses)
        
    print(f"Expense with ID {id} updated.")
    
def main():
    parser = argparse.ArgumentParser(description='Expense Tracker')
    subparsers = parser.add_subparsers(dest='command', required=True, help='Available commands')

    add_parser = subparsers.add_parser('add', help='Add new expense')
    add_parser.add_argument('--description', type=str, required=True, help='Description of the expense')
    add_parser.add_argument('--amount', type=float, required=True, help='Amount of the expense')

    list_parser = subparsers.add_parser('list', help='List all expenses')

    summary_parser = subparsers.add_parser('summary', help='Summarize all expenses')
    summary_parser.add_argument('--month', type=int, help='Month for summary')

    delete_parser = subparsers.add_parser('delete', help='Delete expense by Id')
    delete_parser.add_argument('--id', type=int, required=True, help='Id of the expense to delete')

    update_parser = subparsers.add_parser('update', help='Update expense')
    update_parser.add_argument('--id', type=int, required=True, help='Id of the expense to update')
    update_parser.add_argument('--description', type=str, required=True, help='Description of the expense to update')
    update_parser.add_argument('--amount', type=float, required=True, help='Amount of the description to update')

    args = parser.parse_args()
    
    if args.command == 'add':
        add_expense(filename, args.description, args.amount)
    elif args.command == 'list':
        list_expenses(filename)
    elif args.command == 'summary':
        if hasattr(args, 'month') and args.month:
            summary(filename, args.month)
        else:
            summary(filename)
    elif args.command == "delete":
        delete(filename, args.id)
    elif args.command == "update":
        update(filename, args.id, args.description, args.amount)
        
if __name__ == "__main__":
    main()