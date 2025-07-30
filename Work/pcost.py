# pcost.py
#
# Exercise 1.27
def portfolio_cost(filename):
    "Reads Data out of a give file and sums the portfolio costs"
    
    with open(filename, "rt") as f:
        header = next(f)
        amount = 0
        for line in f:
            row = line.split(",")
            try:
                amount += int(row[1]) * float(row[2])
            except ValueError:
                print("Value is not present!")
        return amount
        
cost = portfolio_cost("Data/missing.csv")
print("Total costs:", cost)