# pcost.py
#
# Exercise 1.27
import csv
import sys

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'


def portfolio_cost(filename):
    total_cost = 0
    with open(filename, 'r') as f:
        rows = csv.reader(f)
        header = next(rows)
        try:
            for row in rows:
                # stock = line.split(',')
                total_cost += int(row[-2]) * float(row[-1])
        except ValueError:
            print('Oops:', row)
    return total_cost

cost = portfolio_cost(filename)
print(f'Total cost ${cost:.2f}')  