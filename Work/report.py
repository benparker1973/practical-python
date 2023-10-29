# report.py
#
# Exercise 2.4

import csv
import fileparse


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
    prices = dict(fileparse.parse_csv(price_filename, has_headers=False, types=[str, float]))
    portfolio = fileparse.parse_csv(portfolio_filename, types=[str, int, float])
    report = make_report(portfolio, prices)
    print_report(report)


portfolio_report('Data/portfolio.csv', 'Data/prices.csv')