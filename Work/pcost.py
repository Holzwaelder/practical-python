# pcost.py
#
# Exercise 1.27
from report import read_portfolio

def portfolio_cost(filename):
    "Reads Data out of a give file and sums the portfolio costs"
    
    portfolio = read_portfolio(filename)
    return sum([row["shares"] * row["price"] for row in portfolio])

def main(argv):
    if len(argv) != 2:
        raise SystemExit("2 Arguments must be passed")
    print("Total costs:", portfolio_cost(argv[1]))

if __name__ == "__main__":
    import sys
    main(sys.argv)