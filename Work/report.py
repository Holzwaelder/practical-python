# report.py
#
# Exercise 2.4
from fileparse import parse_csv

def read_portfolio(filename):
    "Reads Data out of a given file and returns a list of tuples"
    
    with open(filename) as lines:
        return parse_csv(lines, select=["name", "shares", "price"], types=[str, int, float])     
    
    
def read_prices(filename):
    "Reads prices out of a given file and returns a dictionary"
    
    with open(filename) as lines:     
        return dict(parse_csv(lines, has_header=False, types=[str, float]))
    
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
    
    portfolio = read_portfolio(file1)
    prices = read_prices(file2)
    report = make_report(portfolio, prices)
    print_report(report)

def main(argv):
    if len(argv) != 3:
        raise SystemExit("Falsche Eingabe in Kommandozeile")
    portfolio_report(argv[1], argv[2])

if __name__ == "__main__":
    import sys
    main(sys.argv)







