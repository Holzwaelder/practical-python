# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
current_month = 0
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    current_month += 1
    
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment    
        
    if extra_payment_start_month <= current_month <= extra_payment_end_month:
        principal -= extra_payment
        total_paid += extra_payment
    
    if principal < 0:
        total_paid += principal
        principal = 0        
    
    print(f"{current_month:<5} {total_paid:<10.2f} {principal:<10.2f}")    

print("Total paid:", round(total_paid, 2))
print("Month", current_month)