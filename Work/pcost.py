# pcost.py
#
# Exercise 1.27
import csv
import sys
import report


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


def calc_total_cost(portfolio):
    total_cost = 0
    for record in portfolio:
        try:
            total_cost += int(record['shares']) * float(record['price'])
        except ValueError:
            print(f'This did not work {record}')
    return total_cost


def main(argv):
    if len(argv) != 2:
        raise SystemExit(f'Usage: {argv[0]} portfolio')
    portfolio = report.read_portfolio(filename=filename)
    cost = calc_total_cost(portfolio=portfolio)
    print(f'Total cost: ${cost:.2f}')

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'


  