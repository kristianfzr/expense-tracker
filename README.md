https://roadmap.sh/projects/expense-tracker

# Expense Tracker

A simple command-line expense tracker application built with Python.

Project from [roadmap.sh](https://roadmap.sh/projects/expense-tracker)

## Features

- ✅ Add expenses with description and amount
- ✅ Update existing expenses
- ✅ Delete expenses by ID
- ✅ View all expenses in a formatted table
- ✅ View expense summaries (total or by month)
- 📊 Data stored in CSV format
- 🎨 Pretty table output for better readability

## Installation

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

### Install from source

1. Clone the repository:
```bash
git clone https://github.com/kristianfzr/expense-tracker.git
cd expense-tracker
```

2. Install dependencies:
```bash
pip install prettytable
```

3. Install the package:
```bash
pip install -e .
```

This will make the `expense-tracker` command available globally.

## Usage

### Add an expense

```bash
expense-tracker add --description "Coffee" --amount 5.50
expense-tracker add --description "Lunch" --amount 12.99
```

**Note:** Use quotes around multi-word descriptions.

### List all expenses

```bash
expense-tracker list
```

Output:
```
+----+------------+-------------+--------+
| ID | Date       | Description | Amount |
+----+------------+-------------+--------+
| 1  | 2024-12-04 | Coffee      | 5.5    |
| 2  | 2024-12-04 | Lunch       | 12.99  |
+----+------------+-------------+--------+
```

### View expense summary

View total of all expenses:
```bash
expense-tracker summary
```

View total for a specific month (1-12):
```bash
expense-tracker summary --month 12
```

### Update an expense

```bash
expense-tracker update --id 1 --description "Breakfast" --amount 8.50
```

### Delete an expense

```bash
expense-tracker delete --id 1
```

## Data Storage

Expenses are stored in a CSV file located at:
```
expense_tracker/data/expenses.csv
```

The CSV file contains the following fields:
- **ID**: Unique identifier for each expense
- **Date**: Date the expense was created/updated (YYYY-MM-DD)
- **Description**: Description of the expense
- **Amount**: Amount spent

## Development

### Project Structure

```
expense-tracker/
├── expense_tracker/
│   ├── __init__.py
│   ├── cli.py          # Main CLI application
│   └── data/           # CSV data storage
├── pyproject.toml      # Modern Python project configuration
└── README.md
```

### Running without installation

If you haven't installed the package, you can run it directly:

```bash
python -m expense_tracker.cli add --description "Test" --amount 10
```

## License

MIT License

## Author

Kristian Kanchev
