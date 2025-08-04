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
        for rown, row in enumerate(rows, start=1):
            report = dict(zip(header, row))
            try:
                stocks = {
                    "name" : report["name"],
                    "shares" : int(report["shares"]),
                    "price" : float(report["price"])
                }                       
                portfolio.append(stocks) 
            except ValueError:
                print(f"Wrong Value in line {rown} -> {row}")
            except KeyError:
                print(f"Wrong key in line {rown} -> {row}")         
        return portfolio
    
def read_prices(filename):
    "Reads prices out of a given file and returns a dictionary"
    
    prices = {}
    
    with open(filename, "rt") as f:
        rows = csv.reader(f)        
        for row in rows:            
            if len(row) == 2 and row[0] and row[1]:
                try:
                    prices[row[0]] = float(row[1])
                except ValueError:
                    print(f"Invalid price for {row[0]}: {row[1]}")              
        return prices
    
def make_report(portfolio, prices):
    "Takes a list of the portfolio as well as a dictionary with prices and return a list of tuple"
    
    report = []
    
    for share in portfolio:
        change = prices[share["name"]] - share["price"]
        report.append((share["name"], int(share["shares"]), float(prices[share["name"]]), change))
    return report

def print_report(reports):
    """
    Takes a report tuple(Name, Shares, Price, Change) and prints it nicely formatted to the screen
    """
    header = ("Name", "Shares", "Price", "Change")
    print("%10s %10s %10s %10s" % header)
    print(f"{'':->10} "*len(header))
    for report in reports:
        #print("%10s %10d %10.2f %10.2f" % report) printf - C like Umsetzung
        print(f"{report[0]:>10} {report[1]:>10d} {f'${report[2]:.2f}':>10} {report[3]:>10.2f}")
        
def portfolio_report(file1, file2):
    """ 
    Takes tow files file1: Portfolio of owned stocks file2: actual price file of stocks and prints the final report with change value
    """    
    print_report(make_report(read_portfolio(file1), read_prices(file2)))
    
portfolio_report("Data/portfolio.csv", "Data/prices.csv")









