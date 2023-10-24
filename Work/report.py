# report.py
#
# Exercise 2.4

import csv
import sys

if len(sys.argv)==2:
    filename = sys.argv[2]
else:
    filename = 'Data/portfolio.csv'

# def read_portfolio(filename):
#     portfolio = []
#     with open(filename, 'rt') as f:
#         rows = csv.reader(f)
#         headers = next(rows)
#         for row in rows:
#             portfolio.append((row[0], int(row[1]), float(row[2]), ))
#     return portfolio

def read_portfolio(filename):
    portfolio = []
    with open (filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            portfolio.append({'name': row[0],
            'shares': row[1],
            'price': row[2],})
    return portfolio