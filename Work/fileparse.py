# fileparse.py
#
# Exercise 3.3
import csv

def parse_csv(filename, select=None, types=None, has_headers=True, delimeter=','):
    '''
    Parse a csv into a list of records
    '''
    with open(filename)as f:
        rows = csv.reader(f, delimiter=delimeter)
        if has_headers:
            headers = next(rows)
        if select:
            indices = [headers.index(column) for column in select]
            headers = select
        else:
            indices = []
        records = []
        for row in rows:
            if not row:
                continue
            if indices:
                row = [row[index] for index in indices]
            if types:
                row = [type(val) for type, val in zip(types, row)]
            if has_headers:
                record = (dict(zip(headers, row)))
            else:
                record = tuple(row)
            records.append(record)

    return records