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
    "Reads prices out of a given file and returns a dictionarie"
    
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
print(f"{'':->10} "*4)
for report in reports:
    #print("%10s %10d %10.2f %10.2f" % report) printf - C like Umsetzung
    print(f"{report[0]:>10} {report[1]:>10d} {f'${report[2]:.2f}':>10} {report[3]:>10.2f}")

"""value_total = 0.0
differ = 0.0
print(f"{'Share':<8}{'Old value':<12}{'New value':<10}")
for share in portfolio:
    value_total += share["shares"] * share["price"]
    differ += share["shares"] * prices[share["name"]]
    print(f"{share['name']:<8}{value_total:<12.2f}{differ:<10.2f}")
    
print(f"Alter Wert: {value_total}")
print(f"Neuer Wert: {differ}")
print(f"Differenz: {differ - value_total:.2f}")"""





