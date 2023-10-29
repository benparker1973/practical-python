# fileparse.py
#
# Exercise 3.3
import csv

def parse_csv(filename, select=None, types=None, has_headers=True, delimeter=',', silence_errors=False):
    '''
    Parse a csv into a list of records
    '''
    if select and not has_headers:
        raise RuntimeError('selecting columns requires headers')
    
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
        for row_num, row in enumerate(rows):
            if not row:
                continue
            if indices:
                row = [row[index] for index in indices]
            if types:
                try:
                    row = [type(val) for type, val in zip(types, row)]
                except ValueError as e:
                    if not silence_errors:
                        print(f"row {row_num}: Can't convert {row}")
                        print(f'row {row_num}: Reason {e}')
            if has_headers:
                record = (dict(zip(headers, row)))
            else:
                record = tuple(row)
            records.append(record)

    return records