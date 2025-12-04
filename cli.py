import os
import csv
import argparse
from pathlib import Path
from datetime import datetime

expense_DIR = Path(__file__).parent / "data"
expense_DIR.mkdir(exist_ok=True)
filename = expense_DIR / "expenses.csv"
fields = ['ID', 'Date', 'Description', 'Amount']

parser = argparse.ArgumentParser(description='Espense Tracker')
parser.add_argument('description', type=str, help='Description of the expense')
parser.add_argument('amount', type=float, help='Amount of the expense')

args = parser.parse_args()

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
    
    next_id = (max((int(t["ID"]) for t in expenses), default=0)) + 1

    expense = {
        "ID": next_id, "Date": datetime.now().strftime("%Y-%m-%d"), "Description": description, "Amount": amount
    }
        
    expenses.append(expense)
        
    with open(filename, "w") as file:
        csvwriter = csv.DictWriter(file, fieldnames=fields)
        csvwriter.writeheader()
        csvwriter.writerows(expenses)
        
    print(expense)
    
if __name__ == "__main__":
    add_expense(filename, args.description, args.amount)