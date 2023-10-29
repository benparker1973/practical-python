# report.py
#
# Exercise 2.4

import csv
import sys


def read_portfolio(filename):
    '''reads in a portfolio csv file
    '''
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
    '''reads in a csv file that has stock prices
    '''
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
    '''compares the portfolio cost to current prices and returns the gain or loss
    '''
    total = 0
    for s in portfolio:
        total += s['shares'] * (price[s['name']] - s['price'])
    return total


def make_report(portfolio, price):
    '''generates a list of stocks in the portfolio
    '''
    report = []
    for s in portfolio:
        chg = price[s['name']] - s['price']
        report.append((s['name'], s['shares'], price[s['name']], chg))
    return report

def print_report(report):
    '''prints a formatted report of stocks
    '''
    header = ('Name', 'Shares','Price', 'Change',)
    print('{:>10s} {:>10s} {:>10s} {:>10s}'.format(*header))
    print('-'*45)
    for name, shares, price, change in report:
        print(f'{name:>10s} {shares:>10d} {f"${price:.2f}":>10} {change:>10.2f}')


def portfolio_report(portfolio_filename, price_filename):
    prices = read_prices(price_filename)
    portfolio = read_portfolio(portfolio_filename)
    report = make_report(portfolio, prices)
    print_report(report)


portfolio_report('Data/portfolio.csv', 'Data/prices.csv')