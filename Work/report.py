# report.py
#
# Exercise 2.4
import csv

def read_portfolio(filename):
    "Reads Data out of a given file and returns a list of tuples"
    
    portfolio = []
    
    with open(filename, "rt") as f:
        rows = csv.reader(f)
        header = next(rows)       
        for row in rows:            
            try:
                portfolio.append({"name": row[0], "shares": int(row[1]), "price": float(row[2])})
            except ValueError:
                print("Value is not present!")
        return portfolio
    
def read_prices(filename):
    "Reads prices out of a given file and returns a list of dictionaries"
    
    prices = []
    
    with open(filename, "rt") as f:
        rows = csv.reader(f)
        header = next(rows)       
        for row in rows:            
            if bool(row[0]) and bool(row[1]):
                prices[row[0]] = row[1]                
        return prices