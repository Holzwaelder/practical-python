# pcost.py
#
# Exercise 1.27
import csv
import sys

def portfolio_cost(filename):
    "Reads Data out of a give file and sums the portfolio costs"
    
    with open(filename, "rt") as f:
        rows = csv.reader(f)
        header = next(rows)
        amount = 0
        for i, row in enumerate(rows, start=1): 
            record = dict(zip(header, row))           
            try:
                amount += int(record["shares"]) * float(record["price"])
            except ValueError:
                print(f"Row {i}: Couldn't convert: {row}")
        return amount

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = "Data/portfolio.csv"
        
cost = portfolio_cost(filename)
print("Total costs:", cost)