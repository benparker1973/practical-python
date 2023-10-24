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
            'shares': int(row[1]),
            'price': float(row[2]),})
    return portfolio


def read_prices(filename):
    prices = {}
    with open(filename, 'r') as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except Exception as err:
                print(f'Error is {err}. What is this {row}?')
    return prices


def gainloss(portfolio, price):
    total = 0
    for s in portfolio:
        total += s['shares'] * (s['price'] - price[s['name']])
    return total

prices = read_prices('Data/prices.csv')
portfolio = read_portfolio(filename)