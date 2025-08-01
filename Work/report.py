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

portfolio = read_portfolio("Data/portfolio.csv")
prices = read_prices("Data/prices.csv")
reports = make_report(portfolio, prices)
header = ("Name", "Shares", "Price", "Change")

print("%10s %10s %10s %10s" % header)
print(f"{'':->10} "*len(header))
for report in reports:
    #print("%10s %10d %10.2f %10.2f" % report) printf - C like Umsetzung
    print(f"{report[0]:>10} {report[1]:>10d} {f'${report[2]:.2f}':>10} {report[3]:>10.2f}")




