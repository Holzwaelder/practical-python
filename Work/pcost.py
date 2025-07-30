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
        for row in rows:            
            try:
                amount += int(row[1]) * float(row[2])
            except ValueError:
                print("Value is not present!")
        return amount

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = "Data/portfolio.csv"
        
cost = portfolio_cost(filename)
print("Total costs:", cost)