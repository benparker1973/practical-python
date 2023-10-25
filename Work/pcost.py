# pcost.py
#
# Exercise 1.27
import csv
import sys


def portfolio_cost(filename):
    total_cost = 0
    with open(filename, 'r') as f:
        rows = csv.reader(f)
        header = next(rows)
        for i, row in enumerate(rows, start=1):
            record = dict(zip(header, row))
            try:
                total_cost += int(record['shares']) * float(record['price'])
            except ValueError:
                print(f'Row {i}: Couldn"t convert: {row}') 
    return total_cost


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print(f'Total cost ${cost:.2f}')  