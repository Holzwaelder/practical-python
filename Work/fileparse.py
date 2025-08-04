# fileparse.py
#
# Exercise 3.3
import csv

def parse_csv(filename, select=None, types=None, has_header=True, delimiter=","):
    """ 
    Parse a .CSV File into a list of records
    """
    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)
                
        # read the file header, if any
        header = next(rows) if has_header else []
            
        # If a column selector was given, find indices of the specified columns
        # Also narrow the set of headers used for resulting dictionaries
        if select:
            indices = [header.index(colname) for colname in select]
            header = select        
                   
        records = []
        for row in rows:
            if not row:     # skip rows with no data
                continue
            
            # Filter the row if specific columns were selected
            if indices:
                row = [row[index] for index in indices]
                
            # Convert columns to given data types
            if types:
                row = [func(val) for func, val in zip(types, row)]
            
            if has_header:
                # Make a dictionary   
                record = dict(zip(header, row))
            else:
                # Make a tuple
                record = tuple(row)
                
            records.append(record)
                      
    return records